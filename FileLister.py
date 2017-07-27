import os
import tkinter
from tkinter import filedialog


def find_directory():
    root = tkinter.Tk()
    original_directory = filedialog.askdirectory(
        parent=root, initialdir="/", title='Please select a directory')
    # print(original_directory)
    return original_directory


def file_list(original_directory, listing=[]):
    if len(original_directory) > 0:
        original_path = original_directory
        if original_path is not None:
            for fileName in os.listdir(original_path):
                # Use os.path.join(pathORG, fileName) to identify file
                # names.
                # os.path will use absolute file name. To
                # check, you have to give full file path
                if os.path.isfile(os.path.join(original_path, fileName)):
                    # print(fileName)
                    # The bottom code drops the extension
                    # print(os.path.splitext(fileName)[0])
                    listing.append(os.path.splitext(fileName)[0])

        if listing == "":
            print("Cannot find files")
        else:
            listing.sort()
            return listing


def directory_list(original_directory, listing=[]):
    if len(original_directory) > 0:
        original_path = original_directory
        if original_path is not None:
            for fileName in os.listdir(original_path):
                # Use os.path.join(pathORG, fileName) to identify file names.
                # os.path will use absolute file name. To
                # check, you have to give full file path
                if os.path.isdir(os.path.join(original_path, fileName)):
                    # print(fileName)
                    # The bottom code drops the extension
                    # print(os.path.splitext(fileName)[0])
                    listing.append(fileName)

        if listing == "":
            print("Cannot find directories")
        else:
            listing.sort()
            return listing


class FileLister:
    # print(directory_list(find_directory()) == file_list(find_directory()))

    print(set(directory_list(""))
          - set(file_list(")))

    
