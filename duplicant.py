"""DupliCant: a command-line duplicate file finder."""
"""Copyright (c) 2026 Daniel Coffland"""

import sys
from pathlib import Path

def main(dir_path):
    """Run the application"""
    print("DupliCant is under construction.")

    # get directory path from command line
    if len(sys.argv) > 1:
        dir_path = sys.argv[1]
    else:
        print("No directory path provided.")
        sys.exit(1)

    dir_path = Path(dir_path)

    # if path does not exist:
    if not (dir_path.exists()):
        # display error
        print("This path is not a valid directory.")
        # stop program
        sys.exit(1)

    
    # if path is not a directory:
    if not (dir_path.is_dir()):
        # display error
        print("The provided path is not a directory.")
        # stop program
        sys.exit(1)
    
    # create empty dictionary called files_by_size
    files_by_size = {}

    # for each file found recursively:
    for path in dir_path.iterdir():
        if path.is_file():
            file_name = path.name

            # try:
            try:
                # get file size
                file_size = int(path.stat().st_size)
                # add file path to list associated with that size
                if file_size in files_by_size:
                    files_by_size[file_size].append(path)
                else:
                    files_by_size[file_size] = path
            # except file access error:
            except:
                print(f"{file_name} requires permissions to access")
                # report or record skipped file
    
    # for each size and path list:
    for size in files_by_size:
        size_list = files_by_size.get(size, [])
        # if path list contains more than one file:
        if len(size_list) > 1:
            # display the size
            # display each path
            print(f"{size}: {size_list}")


if __name__ == "__main__":
    main(None)