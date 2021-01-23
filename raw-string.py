import re
import sys

# Escape Characters are always preceded by a backslash(\)

print("Backslash: \\")
print("New Line char: \\n")

#  RawString - put an “r" or “R" in front of the string.

print(r"This is a backslash: \ and a new line: \n")

# Python raw string treats backslash(\) as a literal character.
# It is useful when we want to have a string that contains backslash(\)
# and don't want it to be treated as an escape character.

my_string = 'Hello\nWorld'
print(my_string)

my_raw_str = r'Hello\nWorld'
print(my_raw_str)

# Not all the raw strings are valid.
# A raw string that contains only a single backslash is not valid.
# Similarly, raw strings with an odd number of ending backslash are also not valid.

# raw_str_one = r'\'
# raw_str_two = r'xyz\'
# raw_str_tree = r'xyz\\\'

# import Python's regular expressions module


# compile a regular expression... note the raw string literal that doesn't have its backslashes escaped

p = re.compile(r'[Ee](\+|-)?[0-9]+')

print(sys.getsizeof('ciao'))
print(sys.getsizeof(r'ciao'))

s = "Hello\tfrom AskPython\nHi"
print(s)

# s is now a raw string
# Here, both backslashes will NOT be escaped.
s = r"Hello\tfrom AskPython\nHi"
print(s)
