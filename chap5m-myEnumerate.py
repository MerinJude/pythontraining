#Itertools
#chain
import itertools



it1 = iter([1, 2, 3])
it2 = iter([4, 5, 6])
print(next(itertools.chain(it1, it2)))
print(next(itertools.chain(it1, it2)))
print(next(itertools.chain(it1, it2)))
print(next(itertools.chain(it1, it2)))
print(next(itertools.chain(it1, it2)))
print(next(itertools.chain(it1, it2)))
#The built-in function enumerate takes an iteratable and returns an iterator over pairs (index, value) for each value in the source.
def integer():
    i=1
    while True:
        yield i
        i=i+1
def enumerate(itera):
    n=integer()
    lis=[]
    tup=()
    for num in n:
        try:
            tup=num,next(itera)
            lis.append(tup)
        except:
            return lis

list=["a", "b", "c"]
print(enumerate(iter(list)))