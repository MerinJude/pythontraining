#Strings basics
print("=" * 40)
print(len("hello world!"))
text=("""This is a multiline string....
      ....
      and the text has "quotes" too""")
print(text)
print("a\nb\nc")

#other datatypes
#list
list1=[1,2,3,"yes"]
print(len(list1))
print(list1[2])
#tuple
cordinate=(1,3)
print(cordinate)
cord_dup=1,2
print(cord_dup)
x,y=2,3 #another tuple assignment
print(x)
print(y)
#dictionaries
dict_eg={"name": "Merin","age":27}
print(dict_eg['name'])
print(dict_eg['age']) #strings to be in single quotes
#sets
set_a={1,2,3,2,1}
print(set_a) #distinct elements only in set
#special values
x=None #special value
y= True #boolean value
print(x,"\n",y)

#type conversions
#print(5+"2") returns type error, type convert 2 as int("2")
print(5+int("2")) #typeconverted
print(str(5)+"2") #typeconverting to string and hence + will give concatenated result
#code to count no. of digits in a number eg: 2 to power 100
print(2**100)
print(len(str(2**100)))

#custom/user defined functions
def square(x): #def funct name(values passed)
    return x*x
print(square(2)+square(4)) #sum of squares of 2 and 4

def sum_of_squares(z,y): #above operation can be generalised to another function
    return square(z)+square(y)
print(sum_of_squares(3,5))

f=square #functions can be assigned, passed as arguments
print(f(2))

def fxy(f,x,y):
    return f(x)+f(y)
print(fxy(square,2,3))
#global and local variables
x = 0
y = 0
def incr(x):
    y = x + 1 #changing local y
    x=x+1 #changing local x
    return y
print(incr(5))
print(x, y) #global unchanged
numcalls = 0
def square(x):
    global numcalls #using global variable numcalls here inside square()
    numcalls = numcalls + 1 #changed global variable
    return x * x
print(square(3))
print(numcalls) #global changed

x = 2
def f(a):
    x = a * a
    return x
y = f(3)
print(x, y)

def difference(x, y):
   return x - y
print(difference(y=2, x=5))

def increment(x, amount=1): #default argument
   return x + amount
print(increment(5))
print(increment(3,2))

#functions using lambda

cube = lambda x: x ** 3 #defines a fn 'cube' that returns cube of x, no return value unlike def fn()
print(fxy(cube, 2, 3))

#min max functions
print(min(3,4))
print(max(3,4))

#upper lower functions
sample="My name is MERIN and I am practising PYTHON"
print(sample.upper())
print(sample.lower())

#WAF to check if 2 strings are same ignoring case
def istrcmp(text1,text2):
    if((text1.lower())==(text2.lower())):
        return True
    else:
        return False
print(istrcmp("HELLO","heLlO"))
print(istrcmp("Merin","heLlO"))

#conditional expressions
print(2<3) #conditional operators <,>,<=,>=,==,!=
print("perl"<"merin") #lexical comparison (alphabetical order or not)
print(True and True) #logical operators and, not,or
print(2 < 3 and not 3 > 1) #True and not(True) = False
#if elif else
x = 42
if x < 10:
       print('one digit number')
elif x < 100:
    print('two digit number')
else:
    print('big number')

#lists
x = [1, 2, "hello", "world", ["another", "list"]] #heterogenous list
print(len(x))
print(len(x[2])) #indexing starts from 0

#modules
import time #to get time
print(time.asctime()) #returns current system time