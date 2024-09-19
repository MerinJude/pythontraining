def cat(filenames):
    for f in filenames:
        for line in open(f):
            print(line)
def grep(pattern, filenames):
    for f in filenames:
        for line in open(f):
            if pattern in line:
                print(line, end="")
files=["para.txt","num.py","sample.txt","test.py"]
#cat(files)
grep("a",files)