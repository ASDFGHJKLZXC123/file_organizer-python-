import os
from pathlib import Path

def organize_directory(path):
    for item in os.listdir(path):
        item_path = Path(path) / item
        if item_path.is_dir():
            continue
        file_extension = item_path.suffix.lower()
        if not file_extension:
            directory_name = "NoExtension"
        else:
            directory_name = file_extension[1:].title()
        directory_to_move = Path(path) / directory_name
        directory_to_move.mkdir(exist_ok=True)

        new_location = directory_to_move / item
        item_path.rename(new_location)
        print(f"Moved: {item} to {directory_to_move}")

if __name__ == "__main__":
    directory_path = input()
    organize_directory(directory_path)