from youtube_transcript_api import YouTubeTranscriptApi
import pyperclip
import re


def get_video_id(url):
    match = re.search(r"(?<=v=)[\w-]+|(?<=be/)[\w-]+", url)
    return match.group(0) if match else None


def fetch_transcript(url):
    video_id = get_video_id(url)
    if not video_id:
        return "Invalid YouTube URL"

    title = input("Enter the YouTube video title: ")
    channel = input("Enter the YouTube channel name: ")

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        full_transcript = " ".join([entry["text"] for entry in transcript])

        output = f"""

### Transcript from {title} by {channel}

{full_transcript}

"""
        return output

    except Exception as e:
        return f"Error: {e}"


# Usage
url = input("Enter the YouTube video URL: ")
output = fetch_transcript(url)
pyperclip.copy(output)
print("Output has been copied to your clipboard!")
print("\n\n---\n\n")
print(output)
