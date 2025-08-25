# 1. String to Number
from timeit import timeit

num = int("123")       # 123
price = float("45.67")   # 45.67
adult = bool("True")     # True (truthy string → True)

# 2. String to List / Tuple / Set
converted_list = list("123")          # ['1', '2', '3']
# converted_list = "1,2,3".split(",")

print(timeit('list("123")'))
print(timeit('"1,2,3".split(",")'))
converted_tuple = tuple("abc")                # ('a', 'b', 'c')
converted_set = set("banana")               # {'a', 'b', 'n'}

print(converted_list)
print(converted_tuple)
print(converted_set)

# 3. JSON Parsing
import json

json_str = '{"name": "Yash", "age": 23}'   #str
data = json.loads(json_str)       # Parse JSON string → dict
json_string = json.dumps(data)    # Convert dict → JSON string

print("Dictionary: ", data)
print("JSON: ", json_string)


# 4. CSV Parsing
import csv

with open("extras/data.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)



