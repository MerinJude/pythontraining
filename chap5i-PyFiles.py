#Write a function to compute the number of python files (.py extension) in a specified directory recursively.
def PyFiles(path):
    dir_list = os.listdir(path) #list of all files in path
    for files in dir_list:
        if ".py" in files:
            print(files)

import os
path = "C:\python training"
PyFiles(path)