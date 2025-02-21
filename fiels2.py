import os

if __name__ == '__main__':
    for dir_entry in os.scandir():
        if os.path.isdir(dir_entry):
            print(dir_entry, "folder")
        if os.path.isfile(dir_entry):
            print(dir_entry,"file")