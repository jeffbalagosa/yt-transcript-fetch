import os
import sys
from youtube_transcript_api import YouTubeTranscriptApi
import pyperclip
from urllib.parse import urlparse, parse_qs
import logging


def get_video_id(url: str) -> str:
    """
    Extract the video ID from a YouTube URL.

    Args:
        url (str): The YouTube URL.

    Returns:
        str: The video ID if found, None otherwise.

    Raises:
        ValueError: If the input is not a string or not a valid YouTube URL.
    """
    if not isinstance(url, str):
        raise ValueError("URL must be a string")

    parsed_url = urlparse(url)
    if "youtube.com" in parsed_url.netloc:
        return parse_qs(parsed_url.query).get("v", [None])[0]
    elif "youtu.be" in parsed_url.netloc:
        return parsed_url.path.lstrip("/")
    else:
        return None


def get_prompt(prompt_name=""):
    """
    Retrieves a prompt from a file in the "prompts" directory.

    Args:
        prompt_name (str, optional): The name of the prompt file (without the ".md" extension). Defaults to an empty string.

    Returns:
        str: The contents of the prompt file, or an empty string if the file is not found or an error occurs.
    """
    if not prompt_name:
        return ""

    if ".." in prompt_name or "/" in prompt_name:
        logging.warning(f"Invalid prompt name: {prompt_name}")
        return ""

    prompt_path = os.path.join("prompts", f"{prompt_name}.md")
    try:
        if os.path.exists(prompt_path):
            with open(prompt_path, "r") as file:
                return file.read().strip()
        else:
            logging.warning(
                f"Prompt file '{prompt_name}.md' not found in the prompts directory."
            )
            return ""
    except IOError as e:
        logging.error(f"Error reading prompt file: {e}")
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
        title_line = f"## Transcript of _{title}_ by {channel}"
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
