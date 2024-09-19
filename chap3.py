# os module
import os
print(os.getcwd())
#urlib module
from urllib.request import urlopen
response = urlopen("http://python.org/")
print(response.headers)
response.headers['Content-Type']

# Write a function make_slug that takes a name converts it into a slug. A slug is a string where spaces and special characters are replaced by a hyphen
def make_slug(name):
    slug = ""
    for lett in name:
        if lett==" ":
            slug=slug+"-"
        elif lett in "!@#$%^&*()_=+-{}11|:;<>,.?/":
            continue
        else:
            slug=slug+lett
    leng=len(slug)
    for i in range(0,leng-1):
        if slug[i]=="-":
            if slug[i-1]=="-":
                slug=slug[:i]+slug[i+1:]
                leng=leng-1
            else:
                continue
        else:
            continue
    print(slug)
name=input(" Enter name: ")
make_slug(name)
#Write a regular expression to validate a phone number.
phone=input("Enter number with country code: ")
if phone[:4]=="0091":
    if len(phone)==14:
        print("Valid number")
    else:
        print("Invalid")
elif phone[:3]=="+91":
    if len(phone)==13:
        print("Valid number")
    else:
        print("Inavlid")
else:
    print("Invalid")
