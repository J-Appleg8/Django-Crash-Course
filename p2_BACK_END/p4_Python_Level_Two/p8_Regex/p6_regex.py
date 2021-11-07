# ##############################################################################################
# REGULAR EXPRESSIONS ##########################################################################

# Resources:
# Check out: http://regexcheatsheet.com/
# [documentation](https://docs.python.org/2/library/re.html#regular-expression-syntax)

# Summary tables:
# (http://www.tutorialspoint.com/python/python_reg_expressions.htm).


####################################################################
# 1.) Searching for Patterns in Text

# re.search() will take the pattern, scan the text, and then returns a Match object
# If no pattern is found, a None is returned.
# To give a clearer picture of this match object, check out the code below:

print("----------- Regex Search -----------------------")
print("")
import re

patterns = ["term1", "term2"]

text = "This is a string with term1, not the other"

for pattern in patterns:
    print("Im searching for " + pattern)

    if re.search(pattern, text):
        print("Match")
    else:
        print("No match")


# This Match object returned by the search() method is more than just a Boolean
# or None, it contains information about the match, including the original input
# string, the regular expression that was used, and the location of the match.
# Let's see the methods we can use on the match object:
print("")
print("----------- Regex Match -----------------------")
print("")

match = re.search("term1", text)
print(match)
print(type(match))
print(match.start())


####################################################################
# 2.) Split with regular expressions

# Note how re.split() returns a list with the term to spit on removed and the
# terms in the list are a split up version of the string. Create a couple of
# more examples for yourself to make sure you understand!
print("")
print("----------- Regex Split -----------------------")
print("")

split_term = "@"
email = "user@gmail.com"
phrase = "What is the domain name of someone with the email: hello@gmail.com"

print(re.split(split_term, email))


####################################################################
# 3.) Finding all instances of a pattern
# You can use re.findall() to find all the instances of a pattern in a string.
print("")
print("----------- Regex Findall -----------------------")
print("")
print(re.findall("match", "Test phrase match in middle"))


####################################################################
# 4.) Pattern re Syntax
# We can use *metacharacters* along with re to find specific types of patterns.
# Since we will be testing multiple re syntax forms, let's create a function
# that will print out results given a list of various regular expressions and
# a phrase to parse:


# There are five ways to express repetition in a pattern:
#
#     1.) A pattern followed by the meta-character * is repeated zero or more times.
#     2.) Replace the * with + and the pattern must appear at least once.
#     3.) Using ? means the pattern appears zero or one time.
#     4.) For a specific number of occurrences, use {m} after the pattern, where
#         m is replaced with the number of times the pattern should repeat.
#     5.) Use {m,n} where m is the minimum number of repetitions and n is the
#         maximum. Leaving out n ({m,}) means the value appears at least m times,
#         with no maximum.


def multi_re_find(patterns, phrase):

    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat, phrase))
        print("\n")


####################################################################
# 5.) Repetitions Syntax
print("")
print("----------- Repetitions Syntax -----------------------")
print("")


rep_phrase = "sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd"

rep_patterns = [
    "sd*",  # s followed by zero or more d's
    "sd+",  # s followed by one or more d's
    "sd?",  # s followed by zero or one d's
    "sd{3}",  # s followed by three d's
    "sd{2,3}",  # s followed by two to three d's
]

multi_re_find(rep_patterns, rep_phrase)


####################################################################
# 6.) Character Sets
# Character sets are used when you wish to match any one of a group of
# characters at a point in the input. Brackets are used to construct character
# set inputs. For example: the input [ab] searches for occurrences of either a or b.

# It makes sense that the first [sd] returns every instance. Also the second
# input will just return any thing starting with an s in this particular case
# of the test phrase input.
print("")
print("----------- Character Sets -----------------------")
print("")

char_phrase = "sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd"
char_patterns = ["[sd]", "s[sd]+"]

multi_re_find(char_patterns, char_phrase)


####################################################################
# 7.) Exclusion
# We can use ^ to exclude terms by incorporating it into the bracket syntax
# notation. For example: [^...] will match any single character not in the
# brackets.

# Use [^!.? ] to check for matches that are not a !,.,?, or space. Add the +
# to check that the match appears at least once, this basically translate into
# finding the words.
print("")
print("----------- Exclusion -----------------------")
print("")

exc_phrase = "This is a string! But it has punctuation. How can we remove it?"
exc_patterns = ["[^!.?]+"]

multi_re_find(exc_patterns, exc_phrase)


####################################################################
# 8.) Character Ranges

# As character sets grow larger, typing every character that should (or should
# not) match could become very tedious. A more compact format using character
# ranges lets you define a character set to include all of the contiguous
# characters between a start and stop point. The format used is [start-end].
#
# Common use cases are to search for a specific range of letters in the alphabet,
#  such [a-f] would return matches with any instance of letters between a and f.
print("")
print("----------- Character Ranges -----------------------")
print("")

char_rng_phrase = "This is an example sentence. Lets see if we can find some letters."

char_rng_patterns = [
    "[a-z]+",  # sequences of lower case letters
    "[A-Z]+",  # sequences of upper case letters
    "[a-zA-Z]+",  # sequences of lower or upper case letters
    "[A-Z][a-z]+",
]  # one upper case letter followed by lower case letters

multi_re_find(char_rng_patterns, char_rng_phrase)


####################################################################
# 9.) Escape Codes

# You can use special escape codes to find specific types of patterns in your data
# Such as digits, non-digits, whitespace and more.

# Escapes are indicated by prefixing the character with a backslash (\).
# Unfortunately, a backslash must itself be escaped in normal Python strings,
# ---and that results in expressions that are difficult to read

# Using raw strings, created by prefixing the literal value with r, for creating regular expressions
# ---eliminates this problem and maintains readability.
print("")
print("----------- Escape Codes -----------------------")
print("")

esc_phrase = "This is a string with some numbers 1233 and a symbol #hashtag"

esc_patterns = [
    r"\d+",  # sequence of digits
    r"\D+",  # sequence of non-digits
    r"\s+",  # sequence of whitespace
    r"\S+",  # sequence of non-whitespace
    r"\w+",  # alphanumeric characters
    r"\W+",  # non-alphanumeric
]

multi_re_find(esc_patterns, esc_phrase)
