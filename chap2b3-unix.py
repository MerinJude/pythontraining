#Implement unix commands head, tail and grep. Head= first 10 lines of file, tail=last 10 lines of a file, grep= takes a string and prints all lines in the file which contain the specified string.
def head(fil):
    text = fil.readlines()
    if len(text) < 10:
        for i in range(len(text)):
            print(text[i])
    else:
        for i in range(10):
            print(text[i])
def tail(fil):
    text=fil.readlines()
    if len(text)<10:
        for i in range(len(text)):
            print(text[i])
    else:
        for i in range(len(text)-11,len(text)-1):
            print(text[i])
def grep(fil,substr):
    text=fil.readlines()
    for ele in text:
        if substr in ele:
            print(ele)
f=open('chap2b.py','r')
head(f)
f.close()
f=open('chap2b.py','r')
tail(f)
f.close()
f=open('chap2b.py','r')
grep(f,"print")
f.close()