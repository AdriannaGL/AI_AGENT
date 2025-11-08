from google.genai import types 
from functions.function_calling import * 
from functions.get_files_info import *
from functions.get_file_content import *
from functions.run_python_file import *
from functions.write_file import *

def call_function(function_call_part: types.FunctionCall, verbose=False):
    
    if verbose == True:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
        
    if function_call_part.name == schema_get_files_info.name:
        result = get_files_info(working_directory="./calculator", **function_call_part.args)
    elif function_call_part.name == schema_get_file_content.name:
        result = get_file_content(working_directory="./calculator", **function_call_part.args)
    elif function_call_part.name == schema_run_python_file.name:
        result = run_python_file(working_directory="./calculator", **function_call_part.args)
    elif function_call_part.name == schema_write_file.name:
        result = write_file(working_directory="./calculator", **function_call_part.args)
    else:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_call_part.name}"},
                )
            ],
        )
    return types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=function_call_part.name,
            response={"result": result},
        )
    ],
)