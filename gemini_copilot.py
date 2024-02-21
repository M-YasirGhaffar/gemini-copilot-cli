import sys
import click
import google.generativeai as genai
import time
import threading
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set your API key here
API_KEY = os.getenv("API_KEY")

SPINNER_FRAMES = ['-', '\\', '|', '/']

def print_spinner(continue_spinning):
    while continue_spinning[0]:
        for frame in SPINNER_FRAMES:
            print('Summoning Gemini Pro for assistance',frame, end='\r')
            time.sleep(0.1)
            if not continue_spinning[0]:
                print('\n')
                break

@click.command()
@click.argument("question")
def gemini_copilot(question):
    """CLI for getting explanations using the Gemini API."""
    
    # Configure API key
    genai.configure(api_key=API_KEY)

    # Initialize GenerativeModel with 'gemini-pro' model
    model = genai.GenerativeModel('gemini-pro')

    # A question to be answered by the model.
    restriction = """A question is coming your way. Please provide an 
    answer that is concise and informative. The response should not 
    exceed a maximum length of 500 characters. Aim to offer the best 
    possible explanation to the question asked. Ensure the answer is 
    relevant to computer-related topics, including but not limited to 
    programming, CLI usage, coding, and debugging. If the question is not 
    relevant, provide a response indicating the mismatch and refrain from 
    generating an answer. And here is the question that you need to answer: """

    continue_spinning = [True]
    spinner_thread = threading.Thread(target=print_spinner, args=(continue_spinning,))
    spinner_thread.start()

    # Generate content for the provided question
    response = model.generate_content(restriction + question)

    # Stop the spinner
    continue_spinning[0] = False
    spinner_thread.join()
    
    # Print the generated content text
    print("-----------------------------\n" + response.text + "\n-----------------------------")

if __name__ == "__main__":
    gemini_copilot()