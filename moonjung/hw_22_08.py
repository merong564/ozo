from pathlib import Path

def is_there_folder(folder_path):
    path = Path(folder_path) / 'new_folder'

    if not path.exists():
        path.mkdir()

is_there_folder(r'C:\rokey\python\ch22')