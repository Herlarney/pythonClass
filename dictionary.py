#                      Python Dictionary
# Similar to dart map, python dictionary is a collection of key-value pairs. Each key is unique and maps to a value. Dictionaries are mutable, meaning you can change their content without changing their identity.
     
#       dict()


thisDict = dict(name='John', nick='Johnny', age=25, city='New York',dob='1995-05-15')
print(f"this is the dict:{thisDict}") 
# to get the list of all the keys
print(f"this is the list of all the keys:{thisDict.keys()}")
# to get the list of all the values
print(f"this is the list of all the values:{thisDict.values()}")
#  Changing the value of a key

thisDict['age'] = 30
print(f"this is the dict after changing the value of age:{thisDict}")
# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.

print(f"this is the list of all the items:{thisDict.items()}")
# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:


if 'age' in thisDict:
    print("Key 'age' is present in the dictionary")
else:
    print("Key 'age' is not present in the dictionary")
#     Update Dictionary
# The update() method will update the dictionary with the items from the given argument.

thisDict.update({'age': 35, 'city': 'Los Angeles'})
print(f"this is the dict after updating the values of age and city:{thisDict}")

    #   Removing items

# There are several methods to remove items from a dictionary:
# 1. pop() method: Removes the item with the specified key name.
thisDict.pop('age')
print(f"this is the dict after removing the key 'age':{thisDict}")
# 2. popitem() method: Removes the last inserted item (in versions before
print(f"this is the dict after removing the last inserted item:{thisDict.popitem()}")

#  Del
del thisDict['city']
print(f"this is the dict after deleting the key 'city':{thisDict}")

# clear() method: Empties the dictionary.

#     #        PYTHON LOOP
# This works the same way as list
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])

#   Loop through both keys and values, by using the items() method:

for x, y in thisdict.items():
  print(x, y)

#      NESTED DICTIONARY
# A nested dictionary is a dictionary that contains other dictionaries, which can be used to store complex
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x, obj in myfamily.items():
    print(f"when x is printd:{x}")
    
    for y in obj:
        print(f"y printed:{y}: {obj[y]}")

