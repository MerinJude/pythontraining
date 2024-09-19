#Write a function treemap to map a function over nested list.
def treemap(f,l,res=None):
    if res is None:
        res = []
    for i in l:
        if isinstance(i,list)==True:
            res.append(treemap(f,i))
        else:
            res.append(f(i))
    return res
fu=lambda x: x*x
y=treemap(fu, [1, 2, [3, 4, [5]]])
print(y)
#Write a function tree_reverse to reverse elements of a nested-list recursively.
def tree_reverse(l,res=None):
    if res is None:
        res=[]
    for i in range(len(l)-1,-1,-1):
        if isinstance(l[i],list)==True:
            res.append(tree_reverse(l[i]))
        else:
            res.append(l[i])
    return res
print(tree_reverse([[1, 2], [3, [4, 5]], 6]))
