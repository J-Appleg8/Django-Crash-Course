# # Lists
# In this section we will learn about:
#     1.) Creating lists
#     2.) Indexing and Slicing Lists
#     3.) Basic List Methods
#     4.) Nesting Lists
#     5.) Introduction to List Comprehensions

# 1.) Creating lists
## Lists can hold many different data types
my_list = [1, 2, 3]
my_list = ["A string", 23, 100.232, "o"]
len(my_list)


# 2.) Indexing and Slicing Lists
my_list = ["one", "two", "three", 4, 5]

# Grab element at index 0
my_list[0]

# Grab index 1 and everything past it
my_list[1:]

# Grab everything UP TO index 3
my_list[:3]

# We can also use + to concatenate lists
my_list + ["new item"]

# Reassign
my_list = my_list + ["add new item permanently"]

# We can also use the * for a duplication method similar to strings:
my_list * 2


# 3.) Basic List Methods
## Python lists tend to be more flexible than arrays in other languages for two reasons:
## They have no fixed size (meaning we don't have to specify how big a list will be)
## And they have no fixed type constraint (like we've seen above).

# Inserts the second list into mylist
mylist = ["a", "b", "c", "d", "e"]
mylist.append(["x", "y", "z"])

# Combines both lists
listtwo = ["a", "b", "c", "d", "e"]
listtwo.extend(mylist)

# Pop method to remove an item from a list - Default removes the last item from list
pop_mylist = ["a", "b", "c", "d", "e"]
item = pop_mylist.pop()

# Specifying an index position of the list for pop()
itemtwo = pop_mylist.pop(0)

# Reversing a list
pop_mylist.reverse()

# Sort List
sort_list = [4, 6, 7, 1, 43, 2]
sort_list.sort()


# 4.) Nesting Lists
## Make a list of lists to form a matrix
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [7, 8, 9]
matrix = [list_1, list_2, list_3]

# Grab first item in matrix object
matrix[0]

# Grab first item of the first item in the matrix object
matrix[0][0]


# 5.) List Comprehensions
# We used list comprehension to grab the first element of every row in the matrix object
first_col = [row[0] for row in matrix]

print(first_col)
