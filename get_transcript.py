from youtube_transcript_api import YouTubeTranscriptApi, get_transcript
from urllib.parse import urlparse, parse_qs
import os
import re

def get_youtube_id(url):
    query = urlparse(url).query
    params = parse_qs(query)
    if 'v' in params:
        return params['v'][0]
    path = urlparse(url).path
    if 'youtu.be' in url:
        return path.split('/')[-1]
    return None

def get_transcript(video_url):
    video_id = get_youtube_id(video_url)
    if not video_id:
        return "Could not extract video ID from URL."

    try:
        transcript_list = get_transcript(video_id)
        transcript = " ".join([entry['text'] for entry in transcript_list])
        return transcript
    except Exception as e:
        return f"Error fetching transcript: {e}"

def create_markdown_file(title, content, output_dir="."):
    sanitized_title = re.sub(r'[^\w\-_\. ]', '', title)
    filename = os.path.join(output_dir, f"{sanitized_title}.md")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# {title}\\n\\n")
        f.write(content)
    return filename

if __name__ == "__main__":
    video_url = os.environ.get("YOUTUBE_VIDEO_URL")
    if not video_url:
        print("Error: YOUTUBE_VIDEO_URL environment variable not set.")
    else:
        transcript_content = get_transcript(video_url)
        if "Error" not in transcript_content and "Could not" not in transcript_content:
            # For simplicity, using video ID as title for now. Can be improved.
            video_id = get_youtube_id(video_url)
            filename = create_markdown_file(f"YouTube Transcript for {video_id}", transcript_content)
            print(f"Transcript saved to {filename}")
        else:
            print(transcript_content)
