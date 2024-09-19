#working with files
f = open('chap1.py', 'r') #read mode
print(f.readline()) #returns one line as a string
#print(f.readlines()) #returns a list of all lines
#print(f.read()) #returns all lines as string
f.close()
f=open('chap2a.py','a') #append mode
#f.write("\n\n#this is a sample text appended while playing with file operations") #appends text to a file
f.close()
f=open('chap2a.py','r')
print(f.read())
f = open('sample.txt','w') #opens a text file sample if already present, or creates a new one
f.writelines(['a\n', 'b\n', 'c\n','d']) #writes the each list elements as a line
f.close()
f=open('sample.txt','r')
#print(f.read())
f.close()
#examples
#compute the number of characters, words and lines in a file.
def chara(filnam):
    return len(filnam.read())
def word(filnam):
    y=filnam.read()
    return len(y.split())
def lines(filnam):
    return len(filnam.readlines())
f=open('sample.txt','r')
print(chara(f))
f.close() #to reset the cursor back to start of file
f=open('sample.txt','r')
print(word(f))
f.close()
f=open('sample.txt','r')
print(lines(f))
f.close()

