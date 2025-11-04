import os

from functions.config import MAX_CHARS 

def get_file_content(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)
    abs_path_dir = os.path.abspath(full_path)
    abs_path_w_d = os.path.abspath(working_directory)
    if not abs_path_dir.startswith(abs_path_w_d):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    
    with open(full_path, "r") as f:
        file_content_string = f.read(MAX_CHARS)
        print(file_content_string)
        if len(file_content_string) >= MAX_CHARS:
            return file_content_string + f'[...File "{file_path}" truncated at {MAX_CHARS} characters].'
        else:
            return file_content_string
