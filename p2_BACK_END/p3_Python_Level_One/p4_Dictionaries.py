# Dictionaries
# This section will consist of:
#     1.) Constructing a Dictionary
#     2.) Accessing objects from a dictionary
#     3.) Nesting Dictionaries
#     4.) Basic Dictionary Methods

# A Python dictionary consists of a key and then an associated value
# That value can be almost any Python object.


#####################################
### 1.) Constructing a Dictionary ###

my_dict = {"key1": "value1", "key2": "value2"}

# Call values by their key
my_dict["key2"]

# Dictionaries are very flexible in the data types they can hold
my_dict = {"key1": 123, "key2": [12, 23, 33], "key3": ["item0", "item1", "item2"]}


###############################################
### 2.) Accessing objects from a dictionary ###
# Call items
access_dict = {"key1": "value1", "key2": "value2"}
access_dict["key3"]

# Call an index on that value
access_dict["key3"][0]

# Call methods on that value
access_dict["key3"][0].upper()

# Affect the values of a key as well
access_dict["key1"]

# Subtract 123 from the value
access_dict["key1"] = access_dict["key1"] - 123

# Check
access_dict["key1"]

# Python also has methods: += (add), -= (subtract), *= (multiply) and /= (divide)
access_dict["key1"] -= 2

# We can also create keys by assignment.
create_dict = {}

# Create a new key through assignment
create_dict["animal"] = "Dog"

# Can do this with any object
create_dict["answer"] = 42


################################
### 3.) Nesting Dictionaries ###
# Dictionary nested inside a dictionary nested in side a dictionary
nested_dict = {"key1": {"nestkey": {"subnestkey": "value"}}}

# Calling the Keys
nested_dict["key1"]["nestkey"]["subnestkey"]


####################################
### 4.) Basic Dictionary Methods ###

# Create a typical dictionary
method_dict = {"key1": 1, "key2": 2, "key3": 3}

# Method to return a list of all keys
method_dict.keys()

# Method to grab all values
method_dict.values()

# Method to return tuples of all items  (we'll learn about tuples soon)
method_dict.items()
