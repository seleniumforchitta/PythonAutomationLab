# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import math
def greet():
    print("Try programiz.pro")

greet()

def add_num(a, b):
    return pow(a,2)+pow(b,2)+2*a*b # (a)2+(b)2+2ab

print(math.sqrt(add_num(34, 54)))


def add_all(*num): # *args in Functions
    return(sum(num))

print(add_all(3, 4, 5, 6, 7, 8))


def add_num(a =6, b=7): # default arguments
    return a+b

print(add_num())


def add_num(a,b):
    return a+b

print(add_num(b=67,a=3)) # keyword arguments


