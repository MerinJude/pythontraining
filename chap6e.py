#Write a function count_change to count the number of ways to change any given amount. Available coins are also passed as argument to the function.
"""def count_change(a,l):
    count=0
    for i in l:
        if a%i==0:
            count+=1
    for x in range(len(l)-1):
        for y in range(x,len(l)):
            q=a/l[x]
            rem=a%l[x]
            if (a-rem)%l[y]==0:
                count+=1
            if
    print(count)
count_change(10,[1,2])
#Write a function permute to compute all possible permutations of elements of a given list.
def permute(lis):
    res=[]
    for a in range(len(lis)):
        for b in range(len(lis)):
            dup = lis
            #print(dup)
            temp=dup[a]
            dup[a]=dup[b]
            dup[b]=temp
            #print(dup)
            res.append(dup)
        #print(res)
    uni_res=[]
    #print(res)
    #for e in res:
        #print(e)
        #if e in uni_res:
            #continue
        #else:
    #       uni_res.append(e)
    print(uni_res)
permute([1, 2, 3])"""

