from functools import reduce
from math import pi

def calc_area(radius):
    return pi * radius**2

area = calc_area(3)
print("Area of circle is: ", area)



# lambda
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
# -------------------------------------------------------------------------------------

# Map, Filter, Reduce

# 1. Double the numbers using map:
# Input: [1, 2, 3, 4] → Output: [2, 4, 6, 8]

doubled_list = list(map(lambda x: x*2, [1,2,3,4]))
print(doubled_list)


# 2. Filter even numbers:
# Input: [5, 8, 13, 22, 35] → Output: [8, 22]

even_list = list(filter(lambda x: x%2==0, [5,8,13,22,35]))
print(even_list)


# 3. Capitalize all words:
# Input: ["apple", "banana", "grape"] → Output: ["Apple", "Banana", "Grape"]

capitalized = list(map(lambda fruit: fruit.capitalize(),["apple", "banana", "grape"] ))
print(capitalized)


# 4. Filter names starting with 'A':
# Input: ["Alice", "Bob", "Arun", "Bella"] → Output: ["Alice", "Arun"]

start_with_A = list(filter(lambda name: name.startswith("A"), ["Alice", "Bob", "Arun", "Bella"]))
print(start_with_A)


# 5. Use reduce to find product of all numbers:
# Input: [2, 3, 4] → Output: 24

product =  reduce(lambda a,b: a*b, [2, 3, 4])
print(product)

# 6. Remove empty strings using filter:
# Input: ["hello", "", "world", "", "python"] → Output: ["hello", "world", "python"]

non_empty_strings = list(filter(lambda word: word.isalpha(), ["hello", "", "world", "", "python"]))
print(non_empty_strings)


# 7. Find the longest word using reduce:
# From a list of words, find the one with the maximum length.

lengths = reduce(lambda a,b: a if len(a)>len(b) else b, ["This", "is", "a", "test", "string"])
print(lengths)


# 8. Square only odd numbers using filter + map:
# Input: [1, 2, 3, 4, 5] → Output: [1, 9, 25]

odds = list(filter(lambda num: num%2!=0, [1, 2, 3, 4, 5]))
squared = list(map(lambda num: num*num, odds))
print(squared)


# 9. Find average using reduce:
# Input: [10, 20, 30, 40] → Output: 25.0

avg = reduce(lambda a,b: (a+b)/2, [10, 20, 30, 40])
print(avg)

# 10. Reverse strings using map:
# Input: ["hello", "world"] → Output: ["olleh", "dlrow"]

rev_words = list(map(lambda word: word[::-1], ["hello", "world"]))
print(rev_words)


# 11. Extract domains from emails using map:
# Input: ["a@gmail.com", "b@yahoo.com"] → Output: ["gmail.com", "yahoo.com"]

filtered_emails = list(map(lambda email: email.split("@")[1], ["a@gmail.com", "b@yahoo.com"]))
print(filtered_emails)


# 12. Filter valid mobile numbers (10 digits only):
# Input: ["9876543210", "1234", "9090909090"] → Output: ["9876543210", "9090909090"]

valid_numbers = list(filter(lambda num: len(num)==10, ["9876543210", "1234", "9090909090"]))
print(valid_numbers)


# 13. Sum of squares of even numbers using filter + map + reduce
# numbers = [1, 2, 3, 4, 5, 6]  Output = 56

# even_nums = list(filter(lambda num: num%2==0, [1, 2, 3, 4, 5, 6] ))
# squares = list(map(lambda num: num*num, even_nums))
# sum_of_nums = reduce(lambda a,b: a+b, squares)
# print(sum_of_nums)

sum_of_nums = reduce(lambda a,b: a+b, map(lambda num: num*num, filter(lambda num: num%2==0, [1, 2, 3, 4, 5, 6])))
print("Sum of numbers is: ", sum_of_nums)



# 14. Flatten a list of lists using reduce:
# Input: [[1, 2], [3, 4], [5]] → Output: [1, 2, 3, 4, 5]

flattened = reduce(lambda a,b: a+b, [[1, 2], [3, 4], [5]] )
print("Flattened list is: ", flattened)


# 15. From a list of student scores, return names of students who scored > 90:
students = [
    {"name": "Yash", "score": 85},
    {"name": "Riya", "score": 92},
    {"name": "Aman", "score": 95},
]
# → Output: ["Riya", "Aman"]


top_students = list(map(lambda s: s["name"], filter(lambda s: s["score"] > 90, students)))
print(top_students)
