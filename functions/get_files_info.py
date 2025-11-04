import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    abs_path_dir = os.path.abspath(full_path)
    abs_path_w_d = os.path.abspath(working_directory)
    if not abs_path_dir.startswith(abs_path_w_d):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    dir_content = os.listdir(full_path)
    new_list = []
    for item in dir_content:
        item_path = os.path.join(full_path, item)
        size = os.path.getsize(item_path)
        is_dir = os.path.isdir(item_path)
        result = f'- {item}: file_size={size}, is_dir={is_dir}'
        new_list.append(result)
    return "\n".join(new_list)
    

