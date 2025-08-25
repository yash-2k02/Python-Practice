# List Comprehension is a concise way to create lists using a single line of code, often replacing the need for for loops when generating new lists.


# 1. Extract only active user emails from a user list
users = [
    {"name": "Yash", "email": "yash@email.com", "active": True},
    {"name": "Andy", "email": "andy@email.com", "active": True},
    {"name": "Arya", "email": "arya@email.com", "active": False}
]

active_emails = [(user["name"], user["email"]) for user in users if user["active"]]
print(active_emails)

# 2. Reading lines from a file and removing newline characters
# with open("data.txt", "r") as file:
#     clean_lines = [line.strip() for line in file]


# 3. Flatten a matrix (2D list into 1D list)
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]
print(flattened)


# 4. Convert string numbers to integers and filter
raw_data = ["10", "25", "error", "35", "20"]
clean_data = [int(x) for x in raw_data if x.isdigit()]
print(clean_data)
# print(raw_data)
# print("IS x digit: ", raw_data[1])

# 5. Filter products with price > 1000
products = [
    {"name": "Laptop", "price": 55000},
    {"name": "Mouse", "price": 500},
    {"name": "Phone", "price": 25000}
]

expensive = [p["name"] for p in products if p["price"] > 1000]
print(expensive)


# 6. Replace negative numbers with 0
numbers = [5, -3, 9, -8, 0, 4]
normalized = [num if num >= 0 else 0 for num in numbers]
print(normalized)


# 7. Get all lowercase words from a paragraph
text = "Welcome to ML Journey with Python"
words = text.split()
lowercase_words = [word.lower() for word in words]
print(lowercase_words)


# 8. Generating IDs or usernames from names
names = ["John Doe", "Riya Sen", "Ajay Mehta"]
usernames = [name.lower().replace(" ", "_") for name in names]
print(usernames)


# 9. Create a dictionary with indices as keys (useful in indexing or mappings)
names = ["Yash", "Arya", "Dev"]
index_map = {i: name for i, name in enumerate(names)}
print(index_map)

# 10. Extract all post titles from API-like response
response = [
    {"id": 1, "title": "Intro to Python"},
    {"id": 2, "title": "Advanced React"},
    {"id": 3, "title": "Docker Basics"}
]

titles = [post["title"] for post in response]
print(titles)