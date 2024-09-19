#tracing a function
def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(13))
def trace(f):
    def g(x):
        print(f.__name__, x)
        value = f(x)
        print('return', repr(value))
        return value
    return g

fib = trace(fib)
print(fib(3))
#Write a function vectorize which takes a function f and return a new function, which takes a list as argument and calls f for every element and returns the result as a list.
def vectorize(f,l):
    res=[]
    t=""
    for i in l:
        t=f(i)
        res.append(t)
    return res
print(vectorize(len,["hello", "world"]))
#[5, 5]
#exec and eval
a=2
print(eval("a * a")) #takes an exp and evaluate it
env = {'a' : 42}
x=0
exec('x = a+1', env) #executes env[x]=43
print(env['x'])