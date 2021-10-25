#####################################
#### PART 6: EXERCISE REVIEW  #######

## Problem 1:
# Given the string:
example_string = "django"

# Use indexing to print out the following:
# 'd'
print(example_string[0])

# 'o'
print(example_string[-1])

# 'djan'
print(example_string[:4])

# 'jan'
print(example_string[1:4])

# 'go'
print(example_string[-2:])
print(example_string[4:])

# Use indexing to reverse the string
print(example_string[::-1])


## Problem 2:
# Given this nested list:
example_list = [3, 7, [1, 4, "hello"]]
print("-------------------------------------------")

# Reassign "hello" to be "goodbye"
example_list[2][2] = "goodbye"
print(example_list)


## Problem 3:
# Using keys and indexing, grab the 'hello' from the following dictionaries:
dict_1 = {"simple_key": "hello"}
dict_2 = {"k1": {"k2": "hello"}}
dict_3 = {"k1": [{"nest_key": ["this is deep", ["hello"]]}]}
print("-------------------------------------------")

print(dict_1["simple_key"])
print(dict_2["k1"]["k2"])
print(dict_3["k1"][0]["nest_key"][1][0])


## Problem 4:
# Use a set to find the unique values of the list below:
mylist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
print("-------------------------------------------")

print(set(mylist))
