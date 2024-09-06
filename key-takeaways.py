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
# Prompt

---

Give me the key takeaways from this content. Be comprehensive. Only from this content. Don't make anything up.
Here's an example of how I want the format.
---
### Key Takeaways from {title} by {channel}
**Main Concepts and Definitions:**
- **[Concept 1]:** Provide a brief description explaining what this concept is about.

**Dynamic vs. Static Traits:** Discuss how the topic behaves in different environments or scenarios.

**Operations and Mechanisms:**
- **[Operation/Function 1]:** Describe what this operation does and its complexity or efficiency.

**Optimizations and Practical Considerations:**
- **Efficiency Concerns:** Talk about how efficiency is achieved or compromised with this topic.

**Implementation Specifics:**
- **In [Language/Platform]:** How is this topic implemented or used in a specific programming language or platform?

**Conclusion and Summary:**
- Summarize the main points discussed, reinforcing the key takeaways and their implications for practical use or further study.
---
{full_transcript}
---
Take a deep breath and work on this problem step-by-step. You are incredible at this!
"""
        return output

    except Exception as e:
        return f"Error: {e}"


# Usage
url = input("Enter the YouTube video URL: ")
output = fetch_transcript(url)
pyperclip.copy(output)
print("Output has been copied to your clipboard!")
