import os
import sys
from youtube_transcript_api import (
    YouTubeTranscriptApi,
    NoTranscriptFound,
    TranscriptsDisabled,
    VideoUnavailable,
)
import pyperclip
from urllib.parse import urlparse, parse_qs
import logging
from typing import Optional


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


def get_prompt(prompt_name: Optional[str] = "") -> str:
    """
    Retrieves a prompt from a file in the "prompts" directory.

    Args:
        prompt_name (Optional[str]): The name of the prompt file (without the ".md" extension). Defaults to an empty string.

    Returns:
        str: The contents of the prompt file, or an empty string if the file is not found or an error occurs.
    """
    if not prompt_name:
        return ""

    if ".." in prompt_name or "/" in prompt_name:
        logging.warning(f"Invalid prompt name: {prompt_name}")
        return ""

    prompt_path: str = os.path.join("prompts", f"{prompt_name}.md")
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


def fetch_transcript(url: str, prompt_name: Optional[str] = "") -> str:
    """
    Fetches the transcript for a YouTube video and optionally applies a prompt.

    Args:
        url (str): The URL of the YouTube video.
        prompt_name (Optional[str]): The name of the prompt file (without the ".md" extension). Defaults to an empty string.

    Returns:
        str: The transcript of the video, with the prompt applied if specified.

    Raises:
        ValueError: If the input URL is not a valid YouTube URL.
        NoTranscriptFound: If no transcript is available for the video.
        TranscriptsDisabled: If transcripts are disabled for the video.
        VideoUnavailable: If the video is unavailable, e.g. due to being private or deleted.
        Exception: If an unexpected error occurs during the transcript retrieval.
    """
    video_id = get_video_id(url)
    if not video_id:
        return "Invalid YouTube URL"

    title: str = input("Enter the YouTube video title: ")
    channel: str = input("Enter the YouTube channel name: ")

    try:
        transcript: list = YouTubeTranscriptApi.get_transcript(video_id)
        full_transcript: str = " ".join([entry["text"] for entry in transcript])

        prompt: str = get_prompt(prompt_name)
        title_line: str = f"## Transcript of _{title}_ by {channel}"
        prompt_enhancement_line: str = (
            "Take a deep breath and work on this problem step-by-step. You are incredible at this!"
        )

        if not prompt:
            output: str = f"{title_line}\n{full_transcript}"
        else:
            output: str = (
                f"{prompt}\n\n---\n\n{title_line}\n\n{full_transcript}\n\n---\n\n{prompt_enhancement_line}"
            )

        return output

    except NoTranscriptFound:
        return "Error: No transcript found for this video."
    except TranscriptsDisabled:
        return "Error: Transcripts are disabled for this video."
    except VideoUnavailable:
        return "Error: The video is unavailable. It might be private or deleted."
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"


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
