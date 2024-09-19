#Ierations
#for dictionaries, looping occurs over keys:
for k in {"x": 1, "y": 2}:
    print(k)
#over files
for line in open("para.txt"):
    print(line)
print()
print(",".join(["a", "b", "c"]))
print(",".join({"x": 1, "y": 2}))
print(list("python"))
print(list({"x": 1, "y": 2}))
#iteration protocol
x = iter([1, 2, 3])
print(x)
print(next(x))
print(next(x))
print(next(x))
#print(next(x)) throws StopIteration exception