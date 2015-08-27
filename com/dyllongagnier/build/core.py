from pathlib import Path
from collections import deque

def get_files(directory, recursive=True, ext=None):
    current = Path(directory)
    if not current.is_dir():
        raise ValueError("Input path to get_files must be a directory.")
    files = list()
    queue = deque()
    def parse_file(file_x):
        assert file_x.is_dir()
        sub_files = file_x.iterdir()
        for sub_file in sub_files:
            if sub_file.is_dir():
                queue.append(sub_file)
            elif ext == None or sub_file.suffix == ext:
                files.append(str(sub_file))
    parse_file(current)
    if not recursive:
        return files
    while(len(queue) != 0):
        parse_file(queue.popleft())
    return files
