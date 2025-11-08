import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from functions.function_calling import *


def main():
    print("Hello from ai-agent")

if __name__ == "__main__":
    main()

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

if len(sys.argv) <= 1: 
    print("Eror message")
    sys.exit(1)

user_prompt = sys.argv[1] #sys.argv to lista strigow -plik i tekst, sprawdzamy cala liste!!!!    

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents=messages,
    config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),
)
calls = response.function_calls

if len(sys.argv) >=3 and sys.argv[2] == "--verbose":
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    #print(response.text)


if len(calls) > 0:
    for function_call_part in calls:
        print(f"Calling function: {function_call_part.name}({function_call_part.args}")

else:
    print(response.text)


