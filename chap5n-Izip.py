#Implement a function izip that works like itertools.izip.
def izip(lista,listb):
    tup=()
    for i in range(len(lista)):
        tup=(lista[i],listb[i])
        print(tup)
izip(["a", "b", "c"], [1, 2, 3])