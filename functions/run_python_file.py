import os
import subprocess

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))
        
        if os.path.commonpath([abs_working_dir, abs_target_file]) != abs_working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(abs_target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", abs_target_file]
        
        if args:
            command.extend(args)
        
        completion = subprocess.run(
            command, 
            cwd=abs_working_dir, 
            capture_output=True, 
            text=True, 
            timeout=30
        )

        output: list[str] = []
        
        if completion.returncode != 0:
            output.append(f"Process exited with code {completion.returncode}")
        if not completion.stdout and not completion.stderr:
            output.append ("No output produced")
        if completion.stdout:
            output.append(f"STDOUT: {completion.stdout}")
        if completion.stderr:
            output.append(f"STDERR: {completion.stderr}")
        
        return "\n".join(output)
    
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a Python file within the working directory and returns its output",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the Python file to run, always relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "description": "Optional list of arguments to pass to the Python script",
                },
            },
        },
    },
}