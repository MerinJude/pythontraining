#generator expressions
a = (x*x for x in range(10))
print(a)
print(sum(a))
#find first 10 (or any n) pythogorian triplets. A triplet (x, y, z) is called pythogorian triplet if x*x + y*y == z*z
def integers():
    """Infinite sequence of integers."""
    i = 1
    while True:
        yield i
        i = i + 1
def take(n, seq):
    """Returns first n values from the given sequence."""
    seq = iter(seq)
    result = []
    try:
        for i in range(n):
            result.append(next(seq))
    except StopIteration:
        pass
    return result
trip=((x,y,z) for z in integers() for x in range(1,z) for y in range(1,x) if x*x + y*y ==z*z)
print(take(10,trip))