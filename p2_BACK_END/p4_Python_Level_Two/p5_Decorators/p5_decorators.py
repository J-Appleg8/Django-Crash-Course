# ##############################################################################################
# Decorators ###################################################################################

# Decorators can be thought of as functions which modify the "functionality" of
# another function. They help to make your code shorter and more "Pythonic".
# They are also used a lot in Python Web Frameworks, which is why we need to learn
# them.

# #####################################
# Functions Review
# #####################################
print("----------- Function Review -----------------------")
print("")

s = "GLOBAL VARIABLE"


def func():
    # Calling global variable s in the function changes the value of the global variable
    global s
    s = 50
    print(s)


func()
print(s)

# Python functions create a new scope, meaning the function has its own namespace to find variable names
# when they are mentioned within the function.
# We can check for local variables and global variables with the local() and globals() functions.


def localsfunc():
    mylocal = 10
    print(locals())


localsfunc()

# Here we get back a dictionary of all the global variables, many of them are
# predefined in Python. So let's go ahead and look at the keys:

print(globals().keys())


# Note how "s" is there, the Global Variable we defined as a string:

globals()["s"]


# Now lets run our function to check for any local variables in the func()
# (there shouldn't be any)
localsfunc()


# In Python everything is an object
# That means functions are objects which can be assigned labels and passed into other functions.


def hello(name="James"):
    return "Hello " + name


print(hello())


# Assign a label to the function.  Note that we are not using parentheses here
# because we are not calling the function hello, instead we are just putting
# it into the greet variable.
# This assignment is not attached to the original function:

greet = hello

print(greet())


# #####################################
# Functions within functions
# #####################################

# Great! So we've seen how we can treat functions as objects, now lets see how
# we can define functions inside of other functions:
# Note how due to scope, the welcome() function is not defined outside of the
# hello() function. Now lets learn about returning functions from within functions:
print("")
print("----------- Functions Within Functions -----------------------")
print("")


def other_hello(name="James"):
    print("The other_hello() function has been run!")

    def greet():
        return "This string is inside the greet() sub-function"

    def welcome():
        return "This string is inside welcome()"

    print(greet())
    print(welcome())
    print("End of other_hello()")


other_hello()


# #####################################
# Returning Functions
# #####################################

# Lets take a quick look at the code again.
#
# In the if/else clause we are returning greet and welcome, not greet() and welcome().
#
# This is because when you put a pair of parentheses after it, the function
# gets executed; whereas if you don’t put parenthesis after it, then it can be
# passed around and can be assigned to other variables without executing it.
#
# When we write x = hello(), hello() gets executed and because the name is Jose
# by default, the function greet is returned. If we change the statement to
# x = hello(name = "Sam") then the welcome function will be returned. We can
# also do print hello()() which outputs now you are in the greet() function.

print("")
print("----------- Returning Functions -----------------------")
print("")


def return_hello(name="James"):
    print("The other_hello() function has been run!")

    def greet():
        return "This string is inside the greet() sub-function"

    def welcome():
        return "This string is inside welcome()"

    if name == "James":
        return greet
    else:
        return welcome


x = return_hello()

print(x())


# #####################################
# Functions as Arguments
#######################################
# Note how we can pass the functions as objects and then use them within other functions.
# Now lets see how we can pass functions as arguments into other functions:
print("")
print("----------- Functions as Arguments -----------------------")
print("")


def hello():
    return "Hi Jose!"


def other(func):
    print("Other code would go here")
    print(func())


other(hello)


######################################
# Creating a Decorator
######################################

# In the previous example we actually manually created a Decorator. Here we will
# modify it to make its use case clear:
print("")
print("----------- Creating a Decorator -----------------------")
print("")


def new_decorator(func):
    def wrap_func():
        print("Code here before executing func()")
        func()
        print("func() has been called")

    return wrap_func


@new_decorator
def func_needs_decorator():
    print("This function is in need of a decorator")


# func_needs_decorator = new_decorator(func_needs_decorator)
# func_needs_decorator()

func_needs_decorator()
