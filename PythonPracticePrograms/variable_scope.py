# Based on the variable scope there are 3 types of varibale in Python
# 1. Local
# 2. Global
# 3. Non-Local

message = 'Hi' # Global
def method():
    message = 'Hello'
    print(message)

method() # Hello
print(message) # Hi

# Python Nonlocal Variables
# In Python, the nonlocal keyword is used within nested functions to indicate that a variable is not local to the inner function, but rather belongs to an enclosing function’s scope.

# This allows you to modify a variable from the outer function within the nested function, while still keeping it distinct from global variables.

def outer():
    message = 'Hello'
    
    def inner():
        nonlocal message
        
        message = 'Hello World'
        print(message)
        
    inner()
    print(message)
outer()


# Global Keyword = It is used to create a global variable and make changes to the variable in a local context.

c = 1
def num():
    global c
    c = 2
    print(c)
num()


print(c)