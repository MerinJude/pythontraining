#Write an iterator class reverse_iter, that takes a list and iterates it from the reverse direction. ::
from operator import length_hint


class reverse_iter:
    def __init__(self,lis):
        dup=[]
        self.i=0
        self.leng=len(lis)
        for j in range(self.leng-1,-1,-1):
            dup.append(lis[j])
        self.l=dup
    def __next__(self):
        if self.i<self.leng:
            j= self.l[self.i]
            self.i += 1
            return j
        else:
            raise StopIteration()
y=reverse_iter([2,3,5,1,4])
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
#generator
def yrange(n):
    i = 0
    while i < n:
        yield i #generrates values of y
        i += 1
y = yrange(3)
print(next(y))
print(next(y))
print(next(y))
#ex to demonstrate interplay between yield and call to __next__ method
def foo():
    print("begin")
    for i in range(3):
        print("before yield", i)
        yield i #basically a return occurs to main as soon as yield is encountered
        print("after yield", i)
    print("end")
f=foo()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
