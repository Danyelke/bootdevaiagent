import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))
    
        if os.path.commonpath([abs_working_dir, abs_target_file]) != abs_working_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
        if os.path.isdir(abs_target_file):
            return f'Cannot write to "{file_path}" as it is a directory'

        parent_dir = os.path.dirname(abs_target_file)
        os.makedirs(parent_dir, exist_ok=True)

        with open(abs_target_file, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        
    except Exception as e:
        return f"Error: {e}"
    
schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes text content to a specified file within the working directory (overwriting if the file exists)",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to file, relative to the working directory",
                },
                "content": {
                    "type": "string",
                    "description": "Content payload, text value to be written to the file",
                },
            },
        },
    },
}