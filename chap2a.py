#lists
x=range(1,4) #returns a list-like number from 1 upto 4 ie 1,2,3
print(x[2],"\b",len(x))
y=[4,5]
z=[1,2,3,4]
print(z+y) #just like strings
print(y*3)
print(z[-2]) #from last ie second last
print(z[0:2]) #returns a sliced list
print(z[0:-1]) #slices upto last element
print(z[:])#first to last
num=range(10)
num=list(num)
print(num[0:6:2]) #step size by 2
print(num[::-1]) #reverse list
num[0]=10 #mutable
print(num)
print(3 in num)
num.append(11)
print(num)
#example
x = [0, 1, [2]]
x[2][0] = 3
print(x)
x[2].append(4)
print(x)
x[2] = 2
print(x)
#zip function : takes 2 list and returns list of pairs
zip(["a", "b", "c"], [1, 2, 3])
print(zip)
print(sum([1,2]))#sum([])
#Implement a function product, to compute product of a list of numbers.
def product(lis):
    prod=1
    for i in range(len(lis)):
        prod=prod*lis[i]
    return prod
print(product([1,2,3,4]))
#Write a function factorial to compute factorial of a number. use product function from above
def factorial(n):
    list1=range(1,n+1)
    list1=list(list1)
    facto=product(list1)
    return facto
print(factorial(5))
#Write a function reverse to reverse a list without using list slicing
def reverse(lis2):
    lis3=[]
    for i in range(1,len(lis2)+1):
        lis3.append(lis2[-i])
    return lis3
print(reverse([3,4,5,6,1,2]))
print(reverse(reverse([1,2,3])))
#Provide an implementation for min and max functions
def min(var):
    small=var[0]
    for element in var:
        if element<small:
            small=element
    return small
def max(var):
    big=var[0]
    for element in var:
        if element>big:
            big=element
    return big
print(num)
print("min=",min(num))
print("max=",max(num))
words=["apple","cat","zebra","aami"]
print("min=",min(words))
print("max=",max(words))
#  Write a function cumulative_sum to compute cumulative sum of a list [a,a+b,a+b+c,...]
def cumulative_sum(cs_lis):
    dup=[]
    y=0
    for element in cs_lis:
        y=y+element
        dup.append(y)
    return dup
print(cumulative_sum(num))
#Write a function cumulative_product to compute cumulative product of a list of numbers.
def cumulative_pro(cp_lis):
    dup=[]
    y=1
    for element in cp_lis:
        y=y*element
        dup.append(y)
    return dup
print(cumulative_pro([2,3,4,5,8]))
#Write a function unique to find all the unique elements of a list.
def unique(uni_lis):
    uni_list=[]
    for ele in uni_lis:
        if ele not in uni_list:
            uni_list.append(ele)
    return uni_list
print(unique([1,1,3,4,5,3,4,5,6]))
# Write a function dups to find all duplicates in the list.
def dups(dups_lis):
    dup_list=[]
    for i in range(len(dups_lis)):
        if dups_lis[i] in dups_lis[:i]+dups_lis[i+1:]:
            dup_list.append(dups_lis[i])
    return dup_list
print(unique(dups([1,3,4,2,4,6,7,4,5,8,8,9])))
#Write a function group(list, size) that take a list and splits into smaller lists of given size.
def group(l,size):
    count=0
    temp=[]
    grp=[]
    for ele in l:
        if count<size:
            temp.append(ele)
            count=count+1
        if count==size:
            count=0
            grp.append(temp)
            temp=[]
    grp.append(temp)
    return grp
print(group([1,2,3,4,5,6,7,8,9,10], 3))
#Sorting lists
a = [2, 10, 4, 3, 7]
a.sort()
print(a)
a = [4, 3, 5, 9, 2]
print(sorted(a)) #new sorted list
print(a) #no change
a = [[2, 3], [1, 6]]
a.sort()
print(a)
a.sort(key=lambda x: x[1]) #sort based on key ie a fn which returns second element
print(a)
#Write a function lensort to sort a list of strings based on length.
def lensort(lis_str):
    lis_str.sort(key=lambda x: len(x))
    return lis_str
print(lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby']))

#sets
x = {3, 1, 2, 1}
print(x)
x.add(4)
print(x)

#strings
a = "helloworld"
print(a[-2:])
print(a[::-1])
print("hello world".split())
print(" ".join(['hello', 'world']))
print(' hello world\n'.strip()) #leading and traiking white spaces
print('abcdefgh'.strip('abdh'))
print('Chapter %d: %s' % (2, 'Data Structures'))
#Write a function extsort to sort a list of files based on extension
def extsort(lis_files):
    lis_files.sort(key=lambda x: x.split(".")[1])
    return lis_files
print(extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']))


#this is a sample text appended while playing with file operations