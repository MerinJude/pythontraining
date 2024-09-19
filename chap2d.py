#dictionaries
b = {}
b['x'] = 2
b[2] = 'foo'
b[(1, 2)] = 3
print(b)
del b['x']
print(b)
print(b.keys())
print(b.values())
print(b.items())
for key, value in b.items(): print(key, value)
print('foo' in b) #if foo is a key
print(b.setdefault('x', 0)) #returns vaue of key x otherwise sets it to 0
print(b)
print('Chapter %(index)d: %(name)s' % {'index': 2, 'name': 'Data Structures'}) #named parsmeters
#find frequency of all words in a file.
def words_in_file(f):
    wordss=f.read().split()
    return wordss
def frequency_words(f,w):
    freq = {}
    for wor in w:
        freq[wor] = freq.get(wor, 0) + 1
    return freq

f=open('para.txt','r')
w=words_in_file(f)
f.close()
f=open('para.txt','r')
freq=frequency_words(f,w)
print(freq)
f.close()
#Write a program to count frequency of characters in a given file.
def chara_in_file(f):
    wordss=f.read()
    lis=[]
    for ele in wordss:
        lis.append(ele)
    return lis
def frequency_chara(f,w):
    freq = {}
    for wor in w:
        freq[wor] = freq.get(wor, 0) + 1
    return freq

f=open('chap2c.py','r')
w=chara_in_file(f)
f.close()
f=open('chap2c.py','r')
freq=frequency_chara(f,w)
print(freq)
if "#" in freq:
    if ";" in freq:
        print("C program")
    else:
        print("Python program")
else:
        print("Text file")
f.close()

#execution environment
#print(globals())
#print(locals())