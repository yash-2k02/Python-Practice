# Loops in Python with range variations and continue, break and pass keywords

name = "yash"
rev = name[::-1]
# rev = ''.join(reversed(name))
print(rev)


# 1. For loop with strings

s = "yash"
for char in s:
    print(char)

# Using range(len(s)) to Access Index and Character
s = "Python Programming"
for i in range(len(s)):
    print(f"Index {i}: {s[i]}")


# 2. For Loop with range() Variations
print("For loop")

# a. range(stop)
for i in range(5):           # 0 1 2 3 4
    print(i, end=" ")
print()

# b. range(start, stop)
for i in range(2, 6):        #2 3 4 5
    print(i, end=" ")
print()

# c. range(start, stop, step)
for i in range(1, 10, 2):    # 1 3 5 7 9
    print(i, end=" ")
print()

# d. range to loop multiple variables
for i, j in zip(range(5), range(10, 15)):
    print(i, j)

print("While loop")
# 2. while Loop
i = 0
while i < 5:            # 0 1 2 3 4
    print(i, end=" ")
    i += 1
print()

# 3. break Statement  exit loop if condition is satisfied
for i in range(10):      # 0 1 2 3 4
    if i == 5:
        break
    print(i)


# 4. continue Statement   skips a specific iteration
for i in range(5):      # 0 1 3 4
    if i == 2:
        continue
    print(i)

# 5. pass Statement
for i in range(3):
    if i == 1:
        pass            # does nothing - placeholder for future code
    print(i)