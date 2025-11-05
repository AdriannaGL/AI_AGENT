import os

def write_file(working_directory, file_path, content):
    full_path = os.path.join(working_directory, file_path)
    abs_path_dir = os.path.abspath(full_path)
    abs_path_w_d = os.path.abspath(working_directory)
    if not abs_path_dir.startswith(abs_path_w_d):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if os.path.exists(full_path):
        with open(full_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    else:
        dir_name = os.path.dirname(full_path)
        os.makedirs(dir_name, exist_ok=True) #utworz sciezke a jesli istnieje to nic nie rob
        with open(full_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
   
