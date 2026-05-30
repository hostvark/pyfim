import argparse
import logging
from pathlib import Path
from .handlers.dir_handler import sort_directory


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(filename)s] %(levelname)s: %(message)s',
    datefmt='%H:%M:%S'
)


logger = logging.getLogger(__name__)


def check_dir_path(dir_path):
    path = Path(dir_path).resolve()
    if not path.exists():
        raise argparse.ArgumentTypeError(
            f"\nThe path does not exist: {path}"
        )
    if not path.is_dir():
        raise argparse.ArgumentTypeError(
            f"\nFile '{path.name}' is not a directory: {path}"
        )
    return path


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Sorts files into folders based on their type (extension)."
        )
    )
    parser.add_argument(
        "directory",
        nargs="?",
        type=check_dir_path,
        default=Path.cwd(),
        help=(
            "Path to the folder to be sorted "
            "(the current folder by default)"
        )
    )
    args = parser.parse_args()
    sort_directory(args.directory)


if __name__ == "__main__":
    main()
