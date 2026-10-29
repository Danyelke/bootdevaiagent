import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))
        
        if os.path.commonpath([abs_working_dir, abs_target_file]) != abs_working_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(abs_target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(abs_target_file, "r") as f:
            file_content = f.read(MAX_CHARS)
            if f.read(1):
                file_content += (f'[...File "{file_content}" truncated at {MAX_CHARS} characters]')
        return file_content
        
    except Exception as e:
        return f"Error: {e}"
    
schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Reads file content in a specified file path relative to the working directory, providing file content up to a specified length otherwise the output is truncated.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to be read, relative to the working directory",
                },
            },
        },
    },
}