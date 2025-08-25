# List (indexed, mutable, allow duplicates)

# 1. append(): Adds an element to the end of the list.
# 2. copy(): Returns a shallow copy of the list.
# 3. clear(): Removes all elements from the list.
# 4. count(): Returns the number of times a specified element appears in the list.
# 5. extend(): Adds elements from another list to the end of the current list.
# 6. index(): Returns the index of the first occurrence of a specified element.
# 7. insert(): Inserts an element at a specified position.
# 8. pop(): Removes and returns the element at the specified position (or the last element if no index is specified).
# 9. remove(): Removes the first occurrence of a specified element.
# 10. reverse(): Reverses the order of the elements in the list.
# 11. sort(): Sorts the list in ascending order (by default).


nums = [2, 5, 7, 8, 5, 3, 66, 5, 23, 36, 92]

# 1. append()
nums.append(23)  # adding
print("After adding new element", nums)

# 2. copy()
copied_list = nums.copy()
print("Copied list is: ", copied_list)

# 3. clear()
# nums.clear()
# print("List after clearing: ", nums)

# 4. count()
num_count = nums.count(23)
print("Count of 23 is: ", num_count)

# 5. extend()
nums.extend([21,3256,463])
print("List after extending: ", nums)

# 6. index()
print("Index of first 23 is: ", nums.index(23))

# 7. insert()
nums.insert(1, 4)
print("List after inserting at 1st index: ", nums)

# 8. pop()
nums.pop()
print("After popping an element", nums)

# 9. remove()
nums.remove(4)
print("List after removing element", nums)

# 10. reverse()
nums.reverse()
print("Reversed list is: ", nums)

# 11. sort()
nums.sort(reverse=True)
print("Sorted list is: ", nums)

#length
print("Length of list is: ", len(nums))
