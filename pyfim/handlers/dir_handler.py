import shutil
import logging
from pathlib import Path
from .file_handler import get_file_category, rename_file


logger = logging.getLogger(__name__)


def is_cli_path(dir_path):
    cli_path = [
        Path(__file__).resolve().parents[2],
        Path(__file__).resolve().parents[1],
        Path(__file__).resolve().parents[0]
    ]
    return dir_path in cli_path


def sort_directory(dir_path):
    path = Path(dir_path).resolve()

    if not path.exists():
        logger.error("The path does not exist: %s", path)
        return

    if not path.is_dir():
        logger.error(
            "File '%s' is not a directory: %s",
            path.name,
            path
        )
        return

    if is_cli_path(path):
        logger.error(
            "Sorting is forbidden. "
            "The path contains system files of the Pyfim-CLI: %s",
            path
        )
        return

    try:
        files = [f for f in path.iterdir() if f.is_file()]
    except PermissionError:
        logger.error("Directory cannot be read: %s", path)
        return

    if not files:
        logger.info("No files to sort")
        return

    for file in files:
        try:
            category = get_file_category(file)
            new_dir = path / category
            if not new_dir.exists():
                logger.info("New directory has been created: %s",new_dir)
            new_dir.mkdir(exist_ok=True)
        except PermissionError:
            logger.error("No rights to create a folder: %s", new_dir)
            return

        sorted_file = new_dir / file.name
        if sorted_file.exists():
            try:
                rename_file(sorted_file)
            except PermissionError:
                logger.error(
                    "No permissions to move or rename: ",
                    sorted_file
                )
                return

        shutil.move(file, new_dir)
        logger.info("File %s has been moved to %s", file, new_dir)
