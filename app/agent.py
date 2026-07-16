from app.llm import client
import json
from app.config import OLLAMA_MODEL
from app.memory import Memory
from app.prompts import SYSTEM_PROMPT
from app.tools import (
    create_folder,
    create_file,
    write_file,
    read_file,
    list_files,
)

TOOLS = {
    "create_folder": create_folder,
    "create_file": create_file,
    "write_file": write_file,
    "read_file": read_file,
    "list_files": list_files,
}
memory = Memory()


def chat(user_message: str):
    memory.add_user_message(user_message)

    command = user_message.strip()

    # ----------------------
    # Create Folder
    # ----------------------
    if command.lower().startswith("create folder"):
        parts = command.split()
        folder_name = " ".join(parts[2:])

        result = create_folder(folder_name)

        memory.add_assistant_message(result)
        return result

    # ----------------------
    # Write File
    # Example:
    # Write file notes.txt Hello AI Engineer
    # ----------------------
    elif command.lower().startswith("write file"):

        parts = command.split(maxsplit=3)

        if len(parts) < 4:
            return "Usage: Write file filename content"

        file_name = parts[2]
        content = parts[3]

        result = write_file(file_name, content)

        memory.add_assistant_message(result)
        return result

    #create file
    #Example:
    #create file test.txt

    elif command.lower().startswith("create file"):

        parts = command.split(maxsplit=2)

        if len(parts) < 3:
            return "Usage: create file filename"

        file_name = parts[2]

        result = create_file(file_name)

        memory.add_assistant_message(result)

        return result

    # ----------------------
    # Read File
    # Example:
    # Read file notes.txt
    # ----------------------
    elif command.lower().startswith("read file"):

        parts = command.split(maxsplit=2)

        if len(parts) < 3:
            return "Usage: Read file filename"

        file_name = parts[2]

        result = read_file(file_name)

        memory.add_assistant_message(result)
        return result

    # ----------------------
    # List Files
    # Example:
    # List files Demo
    # ----------------------
    elif command.lower().startswith("list files"):

        parts = command.split(maxsplit=2)

        if len(parts) == 2:
            folder = "."
        else:
            folder = parts[2]

        files = list_files(folder)

        result = "\n".join(files)

        memory.add_assistant_message(result)
        return result

    # ----------------------
    # Normal Chat
    # ----------------------

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        }
    ]

    messages.extend(memory.get_messages())

    response = client.chat(
        model=OLLAMA_MODEL,
        messages=messages,
    )

    answer = response["message"]["content"]

    memory.add_assistant_message(answer)

    return answer