import os
import sys
from youtube_transcript_api import YouTubeTranscriptApi
import pyperclip
import re


def get_video_id(url):
    match = re.search(r"(?<=v=)[\w-]+|(?<=be/)[\w-]+", url)
    return match.group(0) if match else None


def get_prompt(prompt_name=""):
    if not prompt_name:
        return ""

    prompt_path = os.path.join("prompts", f"{prompt_name}.md")
    if os.path.exists(prompt_path):
        with open(prompt_path, "r") as file:
            return file.read().strip()
    else:
        print(f"Prompt file '{prompt_name}.md' not found in the prompts directory.")
        return ""


def fetch_transcript(url, prompt_name=""):
    video_id = get_video_id(url)
    if not video_id:
        return "Invalid YouTube URL"

    title = input("Enter the YouTube video title: ")
    channel = input("Enter the YouTube channel name: ")

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        full_transcript = " ".join([entry["text"] for entry in transcript])

        prompt = get_prompt(prompt_name)
        title_line = f"## Transcript of {title} by {channel}"
        prompt_enhancement_line = "Take a deep breath and work on this problem step-by-step. You are incredible at this!"

        if not prompt:
            output = f"{title_line}\n{full_transcript}"
        else:
            output = f"{prompt}\n\n---\n\n{title_line}\n\n{full_transcript}\n\n---\n\n{prompt_enhancement_line}"

        return output

    except Exception as e:
        return f"Error: {e}"


# Usage
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <YouTube URL> [prompt_name]")
        sys.exit(1)

    url = sys.argv[1]
    prompt_name = sys.argv[2] if len(sys.argv) > 2 else ""

    output = fetch_transcript(url, prompt_name)
    pyperclip.copy(output)
    print("Output has been copied to your clipboard!")
    print("\n\n---\n\n")
    print(output)
