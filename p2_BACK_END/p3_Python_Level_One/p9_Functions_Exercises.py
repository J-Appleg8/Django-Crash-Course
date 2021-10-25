##########################################
# PROBLEM 1
##########################################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:
# arrayCheck([1, 1, 2, 3, 1]) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True


# Course Solution:
# Note: iterate with length-2, so can use i+1 and i+2 in the loop
# Check in sets of 3 if we have 1,2,3 in a row
def solution_arrayCheck(nums):

    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
            return True
    return False


##########################################
# PROBLEM 2
##########################################

# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:
# stringBits('Hello') → 'Hlo'
# stringBits('Hi') → 'H'
# stringBits('Heeololeo') → 'Hello'
def stringBits(str):
    str_length = len(str)
    i = 0
    new_str = ""

    while i < str_length:
        if i % 2 == 0 or i == 0:
            new_str = new_str + str[i]
        i += 1

    return new_str


# Course Solution:
# Many ways to do this.
# This uses the standard loop of i on every char, and inside the loop skips the odd index values.
def solution_stringBits(str):
    result = ""

    for i in range(len(str)):
        if i % 2 == 0:
            result = result + str[i]
    return result


##########################################
# PROBLEM 3
##########################################

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True


def end_other(a, b):
    str_a = len(a)
    str_b = len(b)

    if a[-str_b:].lower() == b.lower() or b[-str_a:].lower() == a.lower():
        return True
    else:
        return False


# Course Solutions:
def solution_end_other(a, b):
    a = a.lower()
    b = b.lower()

    return b.endswith(a) or a.endswith(b)


def other_solution_end_other(a, b):
    a = a.lower()
    b = b.lower()

    return a[-(len(b)) :] == b or a == b[-(len(a)) :]


##########################################
# PROBLEM 4
##########################################

# Given a string, return a string where for every char in the original,
# there are two chars.

# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'


def doubleChar(str):
    new_str = ""

    for letter in str:
        temp = letter * 2
        new_str = new_str + temp
    return new_str


# Course Solution
def doubleChar(str):
    result = ""
    for char in str:
        result += char * 2
    return result


##########################################
# PROBLEM 5
##########################################

# Given 3 int values, a b c, return their sum
# However, if any of the values is a teen -- in the range 13-19 inclusive
# Then that value counts as 0, except 15 and 16 do not count as a teens
# Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule.
#
# Examples:
#
# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3


def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)


# Course Solution
def fix_teen(n):
    if n in [13, 14, 17, 18, 19]:
        return 0
    return n


##########################################
# PROBLEM 6
##########################################

# Return the number of even integers in the given array.
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0


def count_evens(nums):
    return len([count for count in nums if count % 2 == 0])


# Course Solution:
def count_evens(nums):
    count = 0
    for element in nums:
        if element % 2 == 0:
            count += 1
    return count
