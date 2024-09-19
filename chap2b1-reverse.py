#Write a program reverse.py to print lines of a file in reverse order.
f=open('chap2b.py','r')
text=f.readlines()
for i in range(len(text)-1,-1,-1):
    print(text[i])
f.close()