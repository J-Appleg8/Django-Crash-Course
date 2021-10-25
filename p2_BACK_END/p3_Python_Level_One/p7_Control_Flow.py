###########################
# LOGICAL OPERATORS
#
# AND
(1 > 2) and (2 < 3)

# OR
(1 > 2) or (2 < 3)

# Multiple logical operators
(1 == 2) or (2 == 3) or (4 == 4)


##################################
# if, elif, else Statements
#
# Indentation is extremely important and is Python's way of not using enclosing brackets {}

# If
if 1 < 2:
    print("Yep!")

if 1 < 2:
    print("yep!")

# If Else
if 1 < 2:
    print("first")
else:
    print("last")

# Elif -  To add more conditions (like else if)
if 1 == 2:
    print("first")
elif 3 == 3:
    print("middle")
else:
    print("Last")


######################################################################
#################### For Loops and While loops #######################

# #############################
# FOR LOOPS
#
# Use For Loops for any sequence of elements
# For loop with a mapping like a dictionary will work, but it won't loop with any order

## For Loop with a list
my_seq = [1, 2, 3, 4, 5, 6]

for item in my_seq:
    print(item)

## For Loop with a Dictionary
print("---------------For Loop ----- Dict---------------------")
ages = {"Sam": 3, "Frank": 4, "Dan": 29}

for item in ages:
    print(item)
    print(ages[item])


# A list of tuple pairs is a very common format for functions to return data in
print("---------------For Loop ----- Tuples---------------------")
mypairs = [(1, 10), (3, 30), (5, 50)]

for item in mypairs:
    print(item)

print("--------------------")
for one, two in mypairs:
    print(one)
    print(two)


# #############################
# WHILE LOOPS
#
# While loops allow us to continually perform and action until a condition becomes true

print("------------------ While Loops ------------------------------")
i = 1
while i < 5:
    print("i is: {}".format(i))
    i += 1


# #############################
# OTHER TOPICS
#
# RANGE FUNCTION
# range() can quickly generate integers for you, based on a starting and ending point
print("------------------ Range Function ------------------------------")

range(5)
print(list(range(5)))

for i in range(5):
    print(i)

# Start and ending
print(list(range(0, 10)))

# Third argument for step-size
print(list(range(0, 10, 2)))


# #############################
# List Comprehension
#
# You can think of this as deconstructing a for loop with an append(). For Example:
# Starting with:
print("------------------ List Comprehension ------------------------------")

x = [1, 2, 3, 4]
out = []

for num in x:
    out.append(num ** 2)

print(out)

# Written in List Comprehension Form
new_list = [item ** 2 for item in x]

print(new_list)

# List Comprehension is a great tool, but remember its not always approriate for
# every situation, don't sacrafice readability for a list Comprehension. It's
# speed is very comparable to the for loop.
