#exceptions and try/except blocks
#as soon as an exception is encountered it immediatley exits the try block
try:
    print(foo)  #raises NameError (foo nt defined)
except NameError:
    print("Name not defined yet",)
try:
    print("foo" + 2)  # raises TypeError (cannot concatenate)
except TypeError:
    print("incompatible types")
try:
    print(2 / 0)  # raises ZeroDivisionError
except ZeroDivisionError:
    print("cannot divide a number by 0")
try:
    print(open("not-there.txt"))  # raises FileNotFoundError
except FileNotFoundError:
    print("No such file exists")
else:
    print("No Exceptions")
finally:
    print("All done, and this will be always executed")

def f():
    try:
        print("a")
        return
    except:
        print("b")
    else:
        print("c")
    finally: #shows that finally will always be executed even if there is a return
        print("d")

f()