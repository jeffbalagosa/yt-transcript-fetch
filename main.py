from youtube_transcript_api import YouTubeTranscriptApi
import re


def get_video_id(url):
    match = re.search(r"(?<=v=)[\w-]+|(?<=be/)[\w-]+", url)
    return match.group(0) if match else None


def fetch_transcript(url):
    video_id = get_video_id(url)
    if not video_id:
        print("Invalid YouTube URL")
        return

    title = input("Enter the YouTube video title: ")
    channel = input("Enter the YouTube channel name: ")

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        full_transcript = " ".join([entry["text"] for entry in transcript])

        print(f"YT Video Title: {title}")
        print(f"YT Video Channel: {channel}\n")
        print(full_transcript)

    except Exception as e:
        print(f"Error: {e}")


url = input("Enter the YouTube video URL: ")
fetch_transcript(url)
