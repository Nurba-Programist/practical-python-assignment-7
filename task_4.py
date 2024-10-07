import os

def find_files_by_extension(directory, extension):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                print(os.path.join(root, file))

find_files_by_extension('/path/to/directory', '.txt')