# lower()	Converts to lowercase
# upper()	Converts to uppercase
# capitalize()	Capitalizes first character
# title()	Capitalizes first letter of each word
# swapcase()	Swaps case of all letters
#
# isalpha()	All characters are letters
# isdigit()	All characters are digits
# isalnum()	Letters and/or digits
# isspace()	Only whitespace
# islower()	All cased chars are lowercase
# isupper()	All cased chars are uppercase
# istitle()	Title case (first letter caps in words)
# startswith(x)	String starts with x
# endswith(x)	String ends with x
#
# strip()    Removes leading / trailing whitespace or chars
# lstrip() Removes leading whitespace / chars
# rstrip() Removes trailing whitespace / chars
#
# find(x)	Returns first index of x or -1
# rfind(x)	Returns last index of x or -1
# index(x)	Like find(), but raises error if not found
# replace(a, b)	Replace all a with b
# count(x)	Counts occurrences of x
#
# split()	Splits string into list
# join(iterable)	Joins elements with string

# ----------------------------------------------------------------------------------

name = "YashPardeshi"
print("Name uppercase: ", name.upper())
print("Name uppercase: ", name.lower())
print("Name capitalize: ", name.capitalize())
print("Name title : ", name.title())
print("Name swapcase: ", name.swapcase())

#----------------------------------------------------------------------------------

print("Name is alphabetic: ", name.isalpha())
print("Name is digit: ", name.isdigit())
print("Name is alphanumeric: ", name.isalnum())
print("Name is space: ", name.isspace())
print("Name is lowercase: ", name.islower())
print("Name is uppercase: ", name.isupper())
print("Name is title: ", name.istitle())
print("Name starts with Y: ", name.startswith(""))
print("Name ends with i: ", name.endswith("i"))

# -----------------------------------------------------------------------------------

name = "        Yash Pardeshi  "
print("Strip: ", name.strip())
print("Left Strip: ", name.lstrip())
print("Right Strip: ", name.rstrip())

#----------------------------------------------------------------------------------

print("Find a: ", name.find("a"))
print("R find a: ", name.rfind("a"))
print("Index of a: ", name.index("a"))
print("Count of a: ", name.count("a"))
print("Replace Y with Z", name.replace("Y", "Z"))

# ----------------------------------------------------------------------------------

message = "Grettings from Python"
name_list = message.split(" ")
print("Split: ", name_list)

name = ["Y", "a", "s", "h"]
name_join = "".join(name)
print("Join: ", name_join)

# ----------------------------------------------------------------------------------