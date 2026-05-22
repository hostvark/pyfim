import yaml
from pathlib import Path
from .datetime_handler import get_file_rename_time


config_path = Path(__file__).resolve().parents[1] / "config.yaml"


def load_yaml(config_path):
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    return config


def get_file_category(file_path):
    config = load_yaml(config_path)
    file_extension = file_path.suffix.lower()
    for file_category, extensions in config.items():
        if file_extension in extensions:
            return file_category
    return "Other"


def rename_file(path):
    file = Path(path).resolve()
    rename_time = get_file_rename_time()

    def inner(file):
        nonlocal rename_time
        stem = file.stem
        suffix = file.suffix.lower()
        parent = file.parent
        new_name = f"{stem}_renamed_on_{rename_time}{suffix}"
        items = [item.name for item in parent.iterdir()]
        if new_name not in items:
            file.rename(parent / new_name)
        else:
            rename_time = get_file_rename_time(delta=1)
            inner(file)
    inner(file)
