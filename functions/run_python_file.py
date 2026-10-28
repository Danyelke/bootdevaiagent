import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        working_directory_abs = os.path.abspath(working_directory)
        target_file_abs = os.path.normpath(os.path.join(working_directory_abs, file_path))
        
        if os.path.commonpath([working_directory_abs, target_file_abs]) != working_directory_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file_abs):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_file_abs]
        
        if args:
            command.extend(args)
        
        completion = subprocess.run(
            command, 
            cwd=working_directory_abs, 
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