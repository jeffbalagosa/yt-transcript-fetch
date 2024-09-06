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
Give me a summary of this content. Be comprehensive. Only from this content. Don't make anything up.

Here's an example of how I want the format.

---
### Summary of "[Title of Document]" by [Author(s)]

**Purpose/Overview:**
- Clearly state the purpose of the document.
- Summarize the main goal or problem it addresses.
- (For "How-to": Focus on the outcome or the main objective of the guide.)

**Background/Context:**
- Provide necessary background or context to understand the topic.
- (For "How-to": Mention any prerequisite knowledge, tools, or skills needed.)

**Key Points/Steps:**
- **[Key Point/Step 1: Title or Description]**:
   - Summarize a key point or step.
   - (For "How-to": Describe the first step in the process, including necessary sub-tasks or details.)

- **[Key Point/Step 2: Title or Description]**:
   - Summarize another key point or step.
   - (For "How-to": Continue outlining steps in the process.)

- **[Continue adding Key Points/Steps]**:
   - For articles, focus on challenges, insights, or arguments presented by the author.
   - For "How-to" guides, keep breaking down the steps, ensuring clarity and order.

**Challenges/Considerations:**
- Summarize challenges or important considerations related to the subject.
- (For "How-to": Include any common mistakes, pitfalls, or key tips that improve efficiency or outcomes.)

**Current/Future Outlook or Expected Outcome:**
- Summarize the current state or expected outcome once the reader follows the guide or understands the topic.
- (For "How-to": Describe the expected result or how to evaluate success after completing the steps.)

**Conclusion/Final Thoughts:**
- Provide a brief conclusion, summarizing key takeaways or final thoughts.
- (For "How-to": Recap any final steps or offer encouragement to complete the process.)

---

Here's the content I needd summarized:

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
print("\n\n---\n\n")
print(output)
