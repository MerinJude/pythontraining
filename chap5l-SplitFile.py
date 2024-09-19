#Write a program split.py, that takes an integer n and a filename as command line arguments and splits the file into multiple small files with each having n lines.
filename=input("Enter the file to be split: ")
split_length=int(input("Enter the split length: "))
f=open(filename)
count=0
num=0
filenam="filesamp"+str(num)+".txt"
files=open(filenam,"w")
for line in f.readlines():
    print(line)
    if count<split_length:
        files.write(line)
        count+=1
    else:
        num += 1
        files.close()
        filenam="filesamp"+str(num)+".txt"
        files=open(filenam,"w")
        count=0
