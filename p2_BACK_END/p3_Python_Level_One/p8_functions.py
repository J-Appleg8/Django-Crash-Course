######################
# FUNCTIONS


def add_num(num1, num2):
    if type(num1) == type(num2) == type(10):
        return num1 + num2
    else:
        return "Not an integer"


result = add_num(1, 3)


# ######################
# Filter Expressions

mylist = [1, 2, 3, 4, 5, 6, 7, 8]


def even_bool(num):
    return num % 2 == 0


evens = filter(even_bool, mylist)
print(list(evens))


# ######################
# Lambda Expressions

evens = filter(lambda num: num % 2 == 0, mylist)
