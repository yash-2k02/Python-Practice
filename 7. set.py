# Set (unordered, mutable)

# Mutating Methods (Modify the Set in Place)
# 1. add(elem)	Adds a given element to the set
# 2. clear()	Removes all elements from the set
# 3. copy()	Returns a shallow copy (non-mutating logically but categorized here due to object manipulation)
# 4. discard(elem)	Removes the element if it exists (no error if not found)
# 5. remove(elem)	Removes the element (raises KeyError if not found)
# 6. pop()	Removes and returns a random element
# 7. update(iterable)	Adds elements from another set or iterable
# 8. difference_update(other)	Removes elements found in another set
# 9. intersection_update(other)	Keeps only elements found in both sets
# 10. symmetric_difference_update(other)	Updates the set with elements found in either set but not in both

# Non-Mutating Methods (Return a New Set)
# difference(other)	Returns elements in the caller but not in the other set
# intersection(other)	Returns elements common to both sets
# union(other)	Returns all elements from both sets
# symmetric_difference(other)	Returns elements in either set but not in both

# Set Comparison / Boolean Methods
# 1. issubset(other)	Checks if caller is a subset of another set
# 2. issuperset(other)	Checks if caller is a superset of another set
# 3. isdisjoint(other)	Checks if two sets have no elements in common

# ------------------------------------------------------------------------------------------------------
s = {1, 2, 3}
print("Original Set:", s)

# 1. add(elem)
s.add(4)
print("After add(4):", s)

# 2. clear()
# s.clear()
# print("After clear():", s)  # Set becomes empty

# 3. copy()
s1 = {10, 20, 30}
s2 = s1.copy()
print("Original:", s1)
print("Copy:", s2)

# 4. discard(elem)
s.discard(5)  # Does nothing since 5 is not in set
print("After discard(5):", s)

# 5. remove(elem)
s.remove(2)  # Removes 2
print("After remove(2):", s)

# 6. pop()
popped = s.pop()
print("Popped element:", popped)
print("After pop():", s)

# 7. update(iterable)
s1 = {1, 2, 3}
s1.update([4, 5], {6, 7}, [10,11])
print("After update:", s1)

# 8. difference_update(other)
s2 = {1, 2, 3, 4, 5}
s2.difference_update([2, 3, 6])
print("After difference_update:", s2)

# 9. intersection_update(other)

s3 = {1, 2, 3, 4}
s3.intersection_update({3, 4, 5})
print("After intersection_update:", s3)

# 10. symmetric_difference_update(other)
s4 = {1, 2, 3}
s4.symmetric_difference_update({2, 3, 4})
print("After symmetric_difference_update:", s4)

# -------------------------------------------------------------------------------------------
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# union() or |
print("a | b:", a | b)  # {1, 2, 3, 4, 5, 6}
print("a.union(b):", a.union(b))

# intersection() or &
print("a & b:", a & b)  # {3, 4}
print("a.intersection(b):", a.intersection(b))

# difference() or -
print("a - b:", a - b)  # {1, 2}
print("a.difference(b):", a.difference(b))

# symmetric_difference() or ^
print("a ^ b:", a ^ b)  # {1, 2, 5, 6}
print("a.symmetric_difference(b):", a.symmetric_difference(b))

# --------------------------------------------------------------------------------------------
x = {1, 2}
y = {1, 2, 3, 4}
z = {5, 6}

# issubset()
print("x.issubset(y):", x.issubset(y))  # True

# issuperset()
print("y.issuperset(x):", y.issuperset(x))  # True

# isdisjoint()
print("x.isdisjoint(z):", x.isdisjoint(z))  # True
print("x.isdisjoint(y):", x.isdisjoint(y))  # False