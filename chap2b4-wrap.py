#Write a program wrap.py that takes filename and width as arguments and wraps the lines longer than width
def wrap(f,width):
    text=f.read()
    count=0
    dup_line=""
    for leters in text:
        if (count<width):
            dup_line=dup_line+leters
            count=count+1
            if dup_line[-1]=="\n":
                print(dup_line)
                count = 0
                dup_line = ""
        if count==width:
            print(dup_line)
            count = 0
            dup_line = ""
files=open('para.txt','r')
wrap(files,30)