import argparse
import logging
from pathlib import Path
from .handlers.dir_handler import sort_directory


root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '%(asctime)s [%(filename)s] %(levelname)s: %(message)s',
    datefmt='%H:%M:%S'
)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)
root_logger.addHandler(console_handler)

logs_dir = Path(__file__).resolve().parents[1] / "logs"
logs_dir.mkdir(exist_ok=True)

file_handler = logging.FileHandler("logs/service.log")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
root_logger.addHandler(file_handler)


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Sorts files into folders based on their type (extension)."
        )
    )
    parser.add_argument(
        "directory",
        nargs="?",
        default=Path.cwd(),
        help=(
            "Path to the folder to be sorted "
            "(current folder by default)"
        )
    )
    args = parser.parse_args()
    sort_directory(args.directory)


if __name__ == "__main__":
    main()
