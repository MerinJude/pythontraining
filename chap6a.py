#recursion
def exp(x, n):
    if n == 0:
        return 1
    else:
        return x * exp(x, n-1)
print(exp(2,3))
def fast_exp(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return fast_exp(x*x, n/2)
    else:
        return x * fast_exp(x, n-1)
print(fast_exp(10,17))
#Implement a function product to multiply 2 numbers recursively using + and - operators only.
def product(a,b):
    if b==0:
        return 0
    else:
        return a+product(a,b-1)
pro=product(10,5)
print(pro)
#flattening a list
def flatten_list(a, result=None):

    if result is None:
        result = []

    for x in a:
        if isinstance(x, list):
            flatten_list(x, result)
        else:
            result.append(x)

    return result
print(flatten_list([ [1, 2, [3, 4] ], [5, 6], 7]))
#Write a function flatten_dict to flatten a nested dictionary by joining the keys with . character.
def flatten_dict(d,reslt=None):
    if reslt is None:
        reslt={}
    for x,y in d.items():
        if isinstance(y,dict):
            k=x+"."
            for (a,b) in y.items():
                reslt[k+a]=b
        else:
            reslt[x]=y
    return reslt
print(flatten_dict(flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})))
#Write a function unflatten_dict to do reverse of flatten_dict.
def unflatten_dict(d,res=None):
    newd={}
    if res==None:
        res={}
    for x,y in d.items():
        if "." in x:
            newd[x]=y
        else:
            res[x]=y
    dict={}
    for k,l in newd.items():
        key=k.split(".")
        dict[key[1]]=l
    res[key[0]]=dict
    #print(res)
    return res
print(unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}))
