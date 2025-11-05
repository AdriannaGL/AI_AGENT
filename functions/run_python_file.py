import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    full_path = os.path.join(working_directory, file_path)
    abs_path_dir = os.path.abspath(full_path)
    abs_path_w_d = os.path.abspath(working_directory)
    if not abs_path_dir.startswith(abs_path_w_d):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found.'
    if not full_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        result = subprocess.run(["python3", file_path]+args, timeout=30, capture_output=True, cwd=abs_path_w_d) #jako args: program ktory chce wykonac + plik + dodatkowe args 
        if result.returncode != 0:
             return f'STDOUT: {result.stdout} STDERR: {result.stderr} Process exited with code {result.returncode}'        
        if result.stdout == "" and result.stderr == "":
            return f'STDOUT: {result.stdout} STDERR: {result.stderr} No output produced'   
        return f'STDOUT: {result.stdout} STDERR: {result.stderr}'
    except Exception as e:
        return f"Error: executing Python file: {e}"

 