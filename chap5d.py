#prints squares of numbers upto a range n
def integers():
    """generates Infinite sequence of integers."""
    i = 1
    while True:
        yield i
        i = i + 1

def squares():
    #generates squares of those infinite sequ of integers
    for i in integers():
        yield i * i

def take(n, seq):
    """Returns first n values from the given sequence."""
    seq = iter(seq) #to initialise iteration
    result = []
    try:
        for i in range(n):
            result.append(next(seq))
    except StopIteration:
        pass
    return result

print(take(5, squares())) # prints [1, 4, 9, 16, 25]
