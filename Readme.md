## Gemini Copilot CLI for Windows

Gemini Copilot CLI for Windows is a command-line tool designed to provide instant assistance on various computer-related topics using the Gemini Pro AI. This tool is specifically tailored for Windows Command Prompt and offers quick answers to questions related to programming, CLI usage, coding, debugging, and more.

### Features

- Get quick explanations on computer-related topics using Gemini Pro AI.
- Easy installation and setup process.
- Designed and tested for Windows Command Prompt.
- Customizable with your own Gemini API key.
- Lightweight and efficient.

### Installation

To install Gemini Copilot CLI, follow these steps:

1. Clone this repository to your local machine.
   ```
   git clone https://github.com/M-YasirGhaffar/gemini-copilot-cli
   ```

2. Navigate to the project directory.
   ```
   cd gemini-copilot-cli
   ```

3. Install the CLI tool using pip.
   ```
   pip install -e .
   ```

### Usage

After installation, you can use the `gemini-copilot` command followed by your question to get assistance from Gemini Copilot CLI. Here's how you can use it:

```
gemini-copilot "Your question here"
```

If you are facing any issues with tool installation, use the code directly:

```
python gemini_copilot.py "Your question here"
```

### Usage Example

![image](https://github.com/M-YasirGhaffar/gemini-copilot-cli/assets/122939183/df7d5299-01e6-47ae-b6fa-0b65e51b7dbd)

### Setting up API Key

To use Gemini Copilot CLI, you need to obtain an API key from the Gemini website. Follow these steps to set up your API key:

1. Go to [ai.google.dev](https://ai.google.dev/tutorials/python_quickstart).
2. Sign up for an account or log in if you already have one.
3. Once logged in, navigate to the API section and generate your API key.
4. Copy the API key and create a `.env` file in the project directory.
5. Inside the `.env` file, add the following line and replace `YOUR_API_KEY` with your actual API key:
   ```
   API_KEY=YOUR_API_KEY
   ```

### Limitations

- Gemini Copilot CLI is designed to provide assistance only on computer-related topics.
- The tool relies on the Gemini Pro model, which may have limitations in its scope of knowledge.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgements

Gemini Copilot CLI is built using the Gemini Pro model from Google.

### Support

For any issues or inquiries, please open an [issue](https://github.com/your_username/gemini-copilot-cli/issues) on GitHub.

### Contribution

Contributions are welcome! Fork the repository, make your changes, and submit a pull request.

### Disclaimer

This tool is provided for informational purposes only. The accuracy and relevance of the information provided by Gemini Copilot CLI may vary and should not be relied upon for critical decision-making.
