# YouTube Transcript Fetcher with Prompt Integration

I took some inspiration from `danielmiessler`'s incredible [Fabric](https://github.com/danielmiessler/fabric.git) project. I've modified it to work with my own needs, since OpenAI's API is not free.

This Python script extracts the transcript from a YouTube video and formats it with a user-defined prompt to use with any LLM chat interface. The final output is copied directly to your clipboard for ease of use. Optionally, you can enhance the output by selecting a predefined prompt from the `prompts` directory.

## Features

- Extracts transcript from a YouTube video.
- Supports both standard YouTube URLs and shortened youtu.be links.
- Optionally includes predefined text prompts stored in the `prompts/` directory.
- Automatically copies the formatted output to your clipboard.

## Requirements

- Python 3.7+
- Virtual environment for isolation
- External libraries from the `requirements.txt` file

## Installation

To get started, follow the instructions for your operating system.

### 1. Clone the repository

```bash
git clone https://github.com/jeffbalagosa/yt-transcript-fetch.git
cd yt-transcript-fetch
```

### 2. Set up a virtual environment

#### On Windows:

1. Open your terminal (Command Prompt or PowerShell).
2. Run the following commands:

```bash
python -m venv venv
.\venv\Scripts\activate
```

#### On MacOS/Linux:

1. Open your terminal.
2. Run the following commands:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

Once your virtual environment is activated, install the required packages:

```bash
pip install -r requirements.txt
```

### 4. (Optional) Add your own prompts to the `prompts` directory

An included `prompts/` directory stores any prompt files you want to use with the script. The prompts should be Markdown files with the `.md` extension (e.g., `prompts/my_prompt.md`).

### 5. Run the script

Use the following command to run the script:

```bash
python main.py <YouTube_URL> [prompt_name]
```

- `<YouTube_URL>`: The URL of the YouTube video.
- `[prompt_name]`: (Optional) The name of a prompt file located in the `prompts/` directory (without the `.md` extension).

For example:

```bash
python main.py https://www.youtube.com/watch?v=dQw4w9WgXcQ extract-wisdom
```

The app will then ask you for additional info, fetch the video transcript, and apply the prompt from `prompts/extract-wisdom.md`.

**Note:** If the prompt argument is omitted, the script will default to just printing the transcript and copying it to your clipboard.

### 6. Clipboard Output

After running the script, the output will be copied directly to your clipboard. Additionally, the full output will be printed to the terminal.

## Logging and Error Handling

The script uses Python's `logging` module to log warnings and errors, such as when a YouTube URL is invalid or a prompt file is not found. The script will return an error message if an error occurs while fetching the transcript.

---

## Disclaimer

Please note that this application is currently a work-in-progress and provided as-is, without any guarantee of support or maintenance. The developer will not provide assistance if you encounter issues while using the app. Additionally, be aware that YouTube may modify their API or website structure at any time, which could potentially affect the functionality of this script. Use at your own discretion and risk.

## License

This project is licensed under the MIT License. See the full license below:

```
MIT License

Copyright (c) 2024 Jeff Balagosa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

Feel free to customize or add additional prompts or enhance the script further.
