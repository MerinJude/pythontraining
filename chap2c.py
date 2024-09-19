#lists
print([(x, y) for x in range(5) for y in range(5) if (x+y)%2 == 0 and x != y]) #multiple for clauses
#print all Pythagorean triplets using numbers below 25. (x, y, z) is a called pythagorean triplet if x*x + y*y == z*z.
print([(x,y,z) for x in range(1,25) for y in range(1,25) for z in range(1,25) if (x*x)+(y*y)==z*z])
#Provide an implementation for zip function using list comprehensions.
def zipfunction(a,b):
    result=[]
    temp=()
    for i in range(len(a)):
        temp=(a[i],b[i])
        result.append(temp)
    return result
print(zipfunction([1,2,3],["a","b","c"]))
#Implementation for map function - applies a function to each element of a list.
def square(x):
    return x*x
def map(f,lis):
    new_lis=[]
    for elem in lis:
        new_lis.append(f(elem))
    return new_lis
print(map(square,range(5)))
#implement filter(f, a) that returns items of the list a for which f(item) returns true
def even(e):
    if e%2==0:
        return True
    else:
        return False
def filter(f,a):
    result=[]
    for ele in a:
        if f(ele)==True:
            result.append(ele)
    print(result)
filter(even,range(10))
#Write a function triplets that takes a number n as argument and returns a list of triplets such that sum of first two elements of the triplet equals the third element using numbers below n. (a,b,c)=(b,a,c)
def triplets(n):
    print([(x,y,z) for x in range(1,n) for y in range(x,n) for z in range(1,n) if x+y==z])
triplets(5)
#Write a function enumerate that takes a list and returns a list of tuples containing (index,item) for each item in the list.
def enumerate(lis):
    new_lis=[]
    for i in range(len(lis)):
        tup=(i,lis[i])
        new_lis.append(tup)
    print(new_lis)
enumerate(["a", "b", "c"])
# Write a function array to create an 2-dimensional array. Value of each element can be initialized to None:
def two_dim_array(a,b):
    array=[]
    temp=[]
    for i in range(a):
        for y in range(b):
            temp.append(None)
        array.append(temp)
        temp=[]
    print(array)
two_dim_array(2,5)
#Write a python function parse_csv to parse csv (comma separated values) files that supports any delimiter and comments.
def parse_csv(f,delim):
    y=f.read().split("\n")
    lis=[]
    for ele in y:
        if '#' not in ele:
            ele=ele.split(delim)
            lis.append(ele)
    return lis
f=open('parse.csv','r')
print(parse_csv(f,"!"))
f.close()
#Write a function mutate to compute all words generated by a single mutation on a given word. A mutation is defined as inserting a character, deleting a character, replacing a character, or swapping 2 consecutive characters in a string.
def mutate(str):
    words=[]
    alpha="abcdefghijklmnopqrstuvwxyz"
    word=""
    for i in alpha:
        word=str+i
        words.append(word)
        word=""
    for j in range(len(str)):
        word=str[:j]+str[j+1:]
        words.append(word)
        word=""
        for letter in alpha:
            word=str[:j]+letter+str[j+1:]
            words.append(word)
            word=""
    for j in range(1,len(str)):
        word=str[:j-1]+str[j]+str[j-1]+str[j+1:]
        words.append(word)
        word=""
    return words
words=mutate("hello")
#print(words)
#Write a function nearly_equal to test whether two strings are nearly equal. Two strings a and b are nearly equal when a can be generated by a single mutation on b.
def nearly_equal(str1,str2):
    if (str1 in mutate(str2)) or (str2 in mutate(str1)):
        return True
    else:
        return False
print(nearly_equal('python', 'perl'))
print(nearly_equal('perl', 'pearl'))
print(nearly_equal('man', 'woman'))
print(nearly_equal('python', 'jython'))