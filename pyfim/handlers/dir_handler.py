import shutil
from pathlib import Path
from .file_handler import get_file_category, rename_file


def sort_directory(dir_path):
    path = Path(dir_path).resolve()

    try:
        files = [f for f in path.iterdir() if f.is_file()]
    except PermissionError:
        print(f"Directory cannot be read: {path}")
        return

    if not files:
        print("No files to sort")
        return

    for file in files:
        try:
            category = get_file_category(file)
            new_dir = path / category
            new_dir.mkdir(exist_ok=True)
        except PermissionError:
            print(f"No rights to create a folder: {new_dir}")
            return

        sorted_file = new_dir / file.name
        if sorted_file.exists():
            try:
                rename_file(sorted_file)
            except PermissionError:
                print(f"No permissions to move or rename: {sorted_file}")
                return

        shutil.move(file, new_dir)
