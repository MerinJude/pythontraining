#Write a program that takes one or more filenames as arguments and prints all the lines which are longer than 40 characters.
def readfiles(files):
    for f in files:
        for line in open(f):
            yield line
def printlines(lines):
    for line in lines:
        if len(line)>40:
            print(line)
filenames=["para.txt","num.py","sample.txt","test.py","chap5g.py"]
line=readfiles(filenames)
printlines(line)