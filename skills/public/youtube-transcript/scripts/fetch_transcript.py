#!/usr/bin/env python3
"""
Fetch YouTube video transcript and save as markdown.

Usage:
    python fetch_transcript.py <youtube_url> [output_file]

Example:
    python fetch_transcript.py "https://www.youtube.com/watch?v=VIDEO_ID" transcript.md
"""

import sys
import re
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound


def extract_video_id(url):
    """
    Extract video ID from various YouTube URL formats.
    """
    patterns = [
        r'(?:youtube\.com\/watch\?v=)([a-zA-Z0-9_-]{11})',
        r'(?:youtu\.be\/)([a-zA-Z0-9_-]{11})',
        r'(?:youtube\.com\/embed\/)([a-zA-Z0-9_-]{11})',
        r'(?:youtube\.com\/v\/)([a-zA-Z0-9_-]{11})'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    
    # If no pattern matches, assume the input is already a video ID
    if re.match(r'^[a-zA-Z0-9_-]{11}$', url):
        return url
    
    raise ValueError(f"Could not extract video ID from: {url}")


def get_transcript(video_id):
    """
    Fetch transcript for a YouTube video.
    Returns list of dictionaries with 'text', 'start', 'duration' keys.
    """
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript_list
    except TranscriptsDisabled:
        raise RuntimeError(f"Transcripts are disabled for video: {video_id}")
    except NoTranscriptFound:
        raise RuntimeError(f"No transcript found for video: {video_id}. Try a different language or auto-generated captions may not be available.")
    except Exception as e:
        raise RuntimeError(f"Error fetching transcript: {e}")


def transcript_to_markdown(transcript, include_timestamps=True):
    """
    Convert transcript to markdown format.
    """
    lines = []
    
    if include_timestamps:
        for entry in transcript:
            start = entry['start']
            minutes = int(start // 60)
            seconds = int(start % 60)
            timestamp = f"[{minutes:02d}:{seconds:02d}]"
            lines.append(f"{timestamp} {entry['text']}")
    else:
        for entry in transcript:
            lines.append(entry['text'])
    
    return "\n\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    url = sys.argv[1]
    
    # Determine output file
    if len(sys.argv) >= 3:
        output_file = sys.argv[2]
    else:
        # Default to video_id.md
        video_id = extract_video_id(url)
        output_file = f"{video_id}.md"
    
    try:
        video_id = extract_video_id(url)
        print(f"Fetching transcript for video ID: {video_id}")
        
        transcript = get_transcript(video_id)
        print(f"Transcript retrieved: {len(transcript)} segments")
        
        markdown_content = transcript_to_markdown(transcript, include_timestamps=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"# YouTube Transcript: {video_id}\n\n")
            f.write(f"URL: {url}\n\n")
            f.write("## Transcript\n\n")
            f.write(markdown_content)
        
        print(f"Transcript saved to: {output_file}")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()