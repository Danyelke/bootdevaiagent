import os

def get_files_info(working_directory: str, directory: str) -> str:
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_target_dir = os.path.normpath(os.path.join(abs_working_dir, directory))
        result = ""

        if os.path.commonpath([abs_working_dir, abs_target_dir]) != abs_working_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(abs_target_dir):
                return f'Error: "{directory}" is not a directory'
        
        for l in os.listdir(abs_target_dir):

            full_path = os.path.join(abs_target_dir, l)

            file_size=os.path.getsize(full_path)
            is_dir=os.path.isdir(full_path)

            result = result + (f" - {l}: file_size={file_size} bytes, is_dir={is_dir}\n")

        return result
    
    except Exception as e:
        return f"Error: {e}"
    
schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}