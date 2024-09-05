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

        print("---")
        print(
            "Give me the key takeaways from this content. Be comprehensive. Only from this content. Don't make anything up."
        )
        print("Here's an example of how I want the format.")
        print("---")
        print(f"### Key Takeaways from {title} by {channel}")
        print(
            "**Main Concepts and Definitions:**\n- **[Concept 1]:** Provide a brief description explaining what this concept is about."
        )
        print(
            "**Dynamic vs. Static Traits:** Discuss how the topic behaves in different environments or scenarios."
        )
        print(
            "**Operations and Mechanisms:**\n- **[Operation/Function 1]:** Describe what this operation does and its complexity or efficiency."
        )
        print(
            "**Optimizations and Practical Considerations:**\n- **Efficiency Concerns:** Talk about how efficiency is achieved or compromised with this topic."
        )
        print(
            "**Implementation Specifics:**\n- **In [Language/Platform]:** How is this topic implemented or used in a specific programming language or platform?"
        )
        print(
            "**Conclusion and Summary:**\n- Summarize the main points discussed, reinforcing the key takeaways and their implications for practical use or further study."
        )
        print("---")
        print(full_transcript)
        print("---")
        print(
            "Take a deep breath and work on this problem step-by-step. You are incredible at this!"
        )

    except Exception as e:
        print(f"Error: {e}")


url = input("Enter the YouTube video URL: ")
fetch_transcript(url)
