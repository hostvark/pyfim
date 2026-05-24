import shutil
from pathlib import Path
from .file_handler import get_file_category, rename_file


def is_cli_path(dir_path):
    path = Path(dir_path).resolve()
    cli_path = [
        Path(__file__).resolve().parents[2],
        Path(__file__).resolve().parents[1],
        Path(__file__).resolve().parents[0]
    ]
    return path in cli_path


def sort_directory(dir_path):
    path = Path(dir_path).resolve()

    if is_cli_path(path):
        print(
            f"Sorting is forbidden.",
            f"The path contains system files of the Pyfim-CLI: {path} ",
            sep="\n"
        )
        return

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
