from pathlib import Path
def create_folder(folder_name: str):
    Path(folder_name).mkdir(parents=True, exist_ok=True)
    return f"Folder '{folder_name}' created successfully."


def create_file(file_name):
    Path(file_name).touch(exist_ok=True)
    return f"File '{file_name}' created successfully."

def list_files(folder_path="."):
    files = [f.name for f in Path(folder_path).iterdir()]
    return files

def write_file(file_name: str, content: str):
    Path(file_name).write_text(content, encoding="utf-8")
    return f"File '{file_name}' written successfully."

def read_file(file_name: str):
    return Path(file_name).read_text(encoding="utf-8")