#Write a function to compute the total number of lines of code, ignoring empty and comment lines, in all python files in the specified directory recursively.
def PyCodes(path):
    TotLen=0
    dir_list=os.listdir(path)
    for files in dir_list:
        if files in PyFiles(dir_list):
            for line in open(files):
                if "#" not in line:
                    if "\"""" not in line:
                            TotLen=TotLen+1
    print(TotLen)
def PyFiles(listdir):
    PyFileList=[]
    for f in listdir:
        if ".py" in f:
            PyFileList.append(f)
    return PyFileList
import os
path="C:\python training"
PyCodes(path)