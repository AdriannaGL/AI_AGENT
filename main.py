import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from functions.function_calling import *
from functions.call_function import *


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
execution_number = 0 
while execution_number <=20:
    execution_number += 1 
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),

    )
    check_candidates = response.candidates
    for candidate in response.candidates:
        messages.append(candidate.content)
    calls = response.function_calls

    verbose = False
    if len(sys.argv) >=3 and sys.argv[2] == "--verbose":
        verbose = True
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        


    if calls is not None and len(calls) > 0: #czy nie jest None
        for function_call_part in calls:
            print(f"Calling function: {function_call_part.name}({function_call_part.args}")
            result = call_function(function_call_part, verbose=verbose)
            try:
                response = result.parts[0].function_response
                messages.append(types.Content(role="user", parts=[types.Part(function_response=response)]))
                if verbose == True:
                    print(f"-> {response.response}")
            except:
                raise Exception("fatal error")
    else:
        print(response.text)
        break #przerywa petle


