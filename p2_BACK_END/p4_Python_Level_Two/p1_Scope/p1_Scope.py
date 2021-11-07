#############################
# Python Scope

# The idea of scope can be described by 3 general rules:
#
# 1. Name assignments will create or change local names by default.
# 2. Name references search (at most) four scopes, these are:
#     * local
#     * enclosing functions
#     * global
#     * built-in
# 3. Names declared in global and nonlocal statements map assigned names to
# enclosing module and function scopes.
#
#
# The statement in #2 above can be defined by the LEGB rule.
#
# **LEGB Rule.**
#
# L: Local — Names assigned in any way within a function (def or lambda)),
# and not declared global in that function.
#
# E: Enclosing function locals — Name in the local scope of any and all
# enclosing functions (def or lambda), from inner to outer.
#
# G: Global (module) — Names assigned at the top-level of a module file, or
# declared global in a def within the file.
#
# B: Built-in (Python) — Names preassigned in the built-in names module :
# open,range,SyntaxError,...


#############################
# Nested Statements and Scope
# When you create a variable name in Python the name is stored in a *name-space*
# Variable names also have a "scope"
# The scope determines the visibility of that variable name to other parts of your code.

print("----------- Nested Statements and Scope -----------------------")

x = 25


def my_func():
    x = 50
    return x


print(x)
print(my_func())


###############################
### Quick examples of LEGB

print("----------- LEGB: Local Example -----------------------")
print("")

print("lambda x: x ** 2")


print("")
print("----------- LEGB: Enclosing function Locals -----------------------")
print("")

name = "This is a global name"


def greet():
    name = "sammy"

    def hello():
        print("Hello " + name)

    hello()


# Does nothing because the print statement is nested inside of the hello() function in greet
# Until we add hello() call inside of the greet function
greet()

# GLOBAL
# Accessible in entire module
print("")
print("----------- LEGB: Global -----------------------")
print("")

print(name)


# BUILT-IN
# These are the built-in function names in Python (don't overwrite these!)
# You will know if you've typed one based on its color!
print("")
print("----------- LEGB: Built-In -----------------------")
print("")

len


# Local Variables

# When you declare variables inside a function definition, they are not related
# in any way to other variables with the same names used outside the function -
# i.e. variable names are local to the function. This is called the scope of the
# variable. All variables have the scope of the block they are declared in
# starting from the point of definition of the name.
#
# Example:
print("")
print("----------- Locals Example Cont. -----------------------")
print("")
xx = 50


def funct(x):
    print("Global xx is ", xx)
    x = 1000
    print("Local xx is changed to ", xx)


funct(xx)
print("Global xx is still {}".format(xx))


# The first print of xx with the first line in the function’s body
# Python uses the value of the parameter declared in the main block, above the function definition.
#
# Next, we assign the value 2 to xx. The name xx is local to our function. So,
# when we change the value of xx in the function, the xx defined in the main block
# remains unaffected.
#
# With the last print statement, we display the value of xx as defined in the main
# block, thereby confirming that it is actually unaffected by the local
# assignment within the previously called function.


################################
# The Global Statement
################################

# If you want to assign a value to a name defined at the top level of the program
# (i.e. not inside any kind of scope such as functions or classes), then you have
# to tell Python that the name is global
# We do this using the global statement
#
# Its impossible to assign a value to a variable defined outside a function
# without the global statement.
#
# You can use the values of such variables defined outside the function
# (assuming there is no variable with the same name within the function).
# However, this is not encouraged and should be avoided since it becomes unclear
# to the reader of the program as to where that variable’s definition is. Using
# the global statement makes it amply clear that the variable is defined
# in an outermost block.
#
# Example:
print("")
print("----------- Globals Example Cont. -----------------------")
print("")

glob = 50


def glob_func():
    global glob
    glob = 1000


print("Before function call, glob is: ", glob)
glob_func()
print("After function call, glob is: ", glob)


# The global statement is used to declare that x is a global variable - hence,
# when we assign a value to x inside the function, that change is reflected
# when we use the value of x in the main block.
#
# You can specify more than one global variable using the same global statement
# e.g. global x, y, z.

###############################
# Conclusion
###############################

# One last mention is that
# you can use the globals() and locals() functions to check what are your current
# local and global variables.
#
# Another thing to keep in mind is that everything in Python is an object! I can
# assign variables to functions just like I can with numbers! We will go over
# this again in the decorator section of the course!
