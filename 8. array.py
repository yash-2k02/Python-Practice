# 1.append(x)	Add value to end
# 2. extend(iterable)	Add all values from iterable
# 3. insert(i, x)	Insert at index
# 4. pop([i])	Remove and return element at index, if no index then last is popped
# 5. remove(x)	Remove first occurrence of x
# 6. index(x)	Get index of x
# 7. count(x)	Count occurrences of x
# 8. fromlist(list)	Append from list
# 9. tolist()	Convert to list

#--------------------------------------------------------------------------------------

from array import array

arr = array("i", [23, 456, 234, 21, 576, 34, 3, 12, 7, 45, 23, 23])
arr.append(1)
for i in range(len(arr)):
    print(i, end=" ")
print()

arr.extend([3,5,6,2])
print("After extend: ", arr)

arr.insert(1,99)
print("After insert: ", arr)

arr.pop()
print("After pop: ", arr)

arr.remove(99)
print("After remove: ", arr)

print("Index of 234: ", arr.index(234))

print("Count of 23: ", arr.count(23))

arr.fromlist([34,545,75])
print("From list: ", arr)

list_from_array = arr.tolist()
print("Converted list is: ", list_from_array)