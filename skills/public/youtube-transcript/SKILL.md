---
name: youtube-transcript
description: "Fetch YouTube video transcripts and save as markdown files in a GitHub repository. Use when you need to: (1) Get a transcript from a YouTube video URL, (2) Save it as a readable markdown file with optional timestamps, (3) Commit and push to a GitHub repository. Requires Python 3 and youtube-transcript-api library."
---

# YouTube Transcript Fetcher

## Overview

This skill provides a Python script to fetch transcripts from YouTube videos using the `youtube-transcript-api` library and save them as formatted markdown files. It handles various YouTube URL formats, extracts video IDs, and can optionally include timestamps. The output can be committed to a GitHub repository.

## Quick Start

### Installation

Ensure you have Python 3 installed, then install the required library:

```bash
pip install youtube-transcript-api
```

### Basic Usage

Run the script with a YouTube URL:

```bash
python scripts/fetch_transcript.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

This will create a file named `VIDEO_ID.md` in the current directory containing the transcript.

### Specify Output File

```bash
python scripts/fetch_transcript.py "https://youtu.be/VIDEO_ID" transcripts/my_video.md
```

### Options

The script accepts two arguments:
1. YouTube URL or video ID (required)
2. Output file path (optional, defaults to `VIDEO_ID.md`)

## Workflow: Save to GitHub Repository

To save the transcript directly into a GitHub repository:

1. **Clone or navigate to your repository**
   ```bash
   cd /path/to/your/repo
   ```

2. **Fetch and save the transcript**
   ```bash
   python /path/to/skill/scripts/fetch_transcript.py "YOUTUBE_URL" docs/transcript.md
   ```

3. **Commit and push**
   ```bash
   git add docs/transcript.md
   git commit -m "Add YouTube transcript for VIDEO_ID"
   git push
   ```

## Script Details

### `scripts/fetch_transcript.py`

The main script provides:

- **Video ID extraction**: Supports multiple YouTube URL formats
- **Transcript fetching**: Uses `youtube-transcript-api` with error handling
- **Markdown formatting**: Includes timestamps by default (format: `[MM:SS] Text`)
- **Error handling**: Reports when transcripts are disabled or unavailable

### Example Output

```markdown
# YouTube Transcript: VIDEO_ID

URL: https://www.youtube.com/watch?v=VIDEO_ID

## Transcript

[00:00] Hello and welcome to this tutorial.
[00:05] Today we'll be learning about Python scripts.
...
```

## Common Issues

### Transcripts Not Available

Some videos have transcripts disabled or only auto-generated captions in certain languages. The script will report `No transcript found` in these cases.

### Installation Problems

If `pip install youtube-transcript-api` fails, ensure you have pip installed and try:

```bash
python -m pip install youtube-transcript-api
```

### Permission Errors

When saving to a GitHub repository, ensure you have write permissions to the directory.

## Integration with OpenClaw

When using this skill within OpenClaw, you can:

1. **Check dependencies** with `exec`:
   ```bash
   python -c "import youtube_transcript_api"
   ```

2. **Run the script** via `exec` with the appropriate workspace path.

3. **Commit changes** using git commands if the workspace is a Git repository.

## Resources

### `scripts/fetch_transcript.py`
The main transcript fetching script. Read this file for implementation details or to modify behavior.

### No additional references or assets needed
This skill is self-contained with a single script.