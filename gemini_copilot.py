import sys
import os
import time
import threading
import re
from dotenv import load_dotenv
from prompt_toolkit import prompt
import google.generativeai as genai
import markdown2

# Load environment variables from .env file
load_dotenv()

# Set your API key here
API_KEY = os.getenv("API_KEY")
SPINNER_FRAMES = ['-', '\\', '|', '/']

def print_spinner(continue_spinning):
    """Loading spinner animation indicating processing."""
    spinner_text = "Processing your request "
    while continue_spinning[0]:
        for frame in SPINNER_FRAMES:
            sys.stdout.write('\r' + spinner_text + frame)
            sys.stdout.flush()
            time.sleep(0.1)
            if not continue_spinning[0]:
                sys.stdout.write('\r' + ' ' * (len(spinner_text) + 1) + '\n')
                sys.stdout.flush()
                break

def get_recent_commands(num_lines=5):
    """Retrieve the last few commands from the log."""
    try:
        with open(os.path.expanduser('~/command_log.txt'), 'r') as file:
            return ''.join(file.readlines()[-num_lines:])
    except Exception as e:
        print(f"Warning: Failed to retrieve command history. Proceeding without it. Error: {e}")
        return ""

def markdown_to_plain_text(markdown_text):
    """Convert Markdown formatted text to plain text suitable for CLI display."""
    # Remove Markdown bold (**text**)
    no_bold = re.sub(r'\*\*(.*?)\*\*', r'\1', markdown_text)
    # Convert Markdown lists to plain text
    no_lists = re.sub(r'\n\*', '\n -', no_bold)
    # Remove any other Markdown links
    clean_text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', no_lists)
    return clean_text

def main():
    """Main function to handle CLI interaction and response formatting."""
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-pro')

    restriction = """This is a command-line interface helper designed to assist with technical queries specifically related to programming, CLI usage, coding, and debugging. Please provide a response that is:
- Concise and directly addresses the user's query.
- Formatted as plain text for easy readability in a command-line environment.
- Limited to a maximum length of 500 characters to ensure clarity and brevity.
- Free from HTML or Markdown formatting.
If the query does not pertain to the aforementioned topics, kindly suggest relevant resources or indicate that the question is outside the scope of this tool's expertise."""

    # Check if a question is provided as a command-line argument
    if len(sys.argv) > 1:
        question = ' '.join(sys.argv[1:])
    else:
        question = prompt('Ask your question: ')

    context = get_recent_commands()
    full_query = f"{context}\nUser Question: {question}" if context else f"User Question: {question}"

    continue_spinning = [True]
    spinner_thread = threading.Thread(target=print_spinner, args=(continue_spinning,))
    spinner_thread.start()

    response = model.generate_content(restriction + full_query)

    continue_spinning[0] = False
    spinner_thread.join()

    formatted_response = markdown_to_plain_text(response.text)
    print("-----------------------------\n" + formatted_response + "\n-----------------------------")

if __name__ == "__main__":
    main()
