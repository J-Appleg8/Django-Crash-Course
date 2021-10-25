#####################################################################################################
############################### Tuples ##############################################################
#####################################################################################################

# Tuples are immutable - meaning they can not be changed
# You would use tuples to present data that shouldn't be changed
# Such as days of the week, or dates on a calendar.
# We can treat them very similarly with the major distinction being that tuples are immutable.

# In this section:
#     1.) Constructing Tuples
#     2.) Basic Tuple Methods
#     3.) Immutability
#     4.) When to Use Tuples.


##############################
## 1.) Constructing Tuples ###

my_tuple = (1, 2, 3)

# Check len just like a list
len(my_tuple)

# Can also mix object types
my_tuple = ("one", 2)

# Use indexing just like we did in lists
my_tuple[0]

# Slicing just like a list
my_tuple[-1]


##############################
## 2.) Basic Tuple Methods ###

# Tuples have built-in methods, but not as many as lists do

# Use .index to enter a value and return the index
my_tuple.index("one")

# Use .count to count the number of times a value appears
my_tuple.count("one")


##############################
## 3.) Immutability ##########

# Because of this immutability, tuples can't grow.
# Once a tuple is made we can not add to it.

my_tuple[0] = "change"

my_tuple.append("nope")


##############################
## 4.) When to use Tuples ####

# Tuples are not used as often as lists in programming, but are used when immutability is necessary
# If in your program you are passing around an object and need to make sure it does not get changed
# Then tuple become your solution. It provides a convenient source of data integrity.


#####################################################################################################
############################### SETS ################################################################
#####################################################################################################

# Sets are an unordered collection of *unique* elements
# We can construct them by using the set() function
my_set = set()

# We add to sets with the add() method
# Note the curly brackets. This does not indicate a dictionary
my_set.add(1)
my_set.add(5)
my_set.add(4)
my_set.add(4)
print(my_set)

# Create a list with repeats
# Cast as set to get unique values
duplicate_list = [1, 1, 2, 2, 3, 4, 5, 6, 1, 1]
unique_sets = set(duplicate_list)
