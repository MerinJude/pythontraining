#Write a program to print each line of a file in reverse order.
f=open('chap2b.py','r')
list_of_lines=f.read()
list_of_lines=list_of_lines.split("\n")
temp=""
for each_line in list_of_lines:
    for i in range(len(each_line)-1,-1,-1):
        temp=temp+each_line[i]
    print(temp)
    temp=""