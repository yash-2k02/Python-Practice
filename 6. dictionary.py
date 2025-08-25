# Dictionary
# key-value pair, indexed, unordered

# 1. clear()    	Removes all the elements from the dictionary
# 2. copy()     	Returns a copy of the dictionary
# 3. fromkeys()	    Returns a dictionary with the specified keys and value
# 4. get()	        Returns the value of the specified key
# 5. items()	    Returns a list containing a tuple for each key value pair
# 6. keys()     	Returns a list containing the dictionary's keys
# 7. values()    	Returns a list of all the values in the dictionary
# 8. pop()	        Removes the element with the specified key
# 9. popitem()	    Removes the last inserted key-value pair
# 10. setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# 11. update()   	Updates the dictionary with the specified key-value pairs

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# 1. clear()
# car.clear()
# print("After clearing dict: ", car)

# 2. copy()
dict_copy = car.copy()
print("Copied dict: ", dict_copy)

# 3. fromkeys()
keys = ['a', 'b', 'c']
d = dict.fromkeys(keys, 0)
print(d)

# 4. get()
print(car.get("brand"))

# 5. items()
print(car.items())

# 6. keys()
print(car.keys())

# 7. values()
print(car.values())

# 8. pop()
car.pop("brand")
print(car)

# 9. popitem()
car.popitem()
print(car)

# 10. update()
car.update({"model": "BMW"})
print(car)
car.update({"city": "Pune"})
print(car)

# 11.setdefault()
x = car.setdefault("model", "Bugatti")
print(x)