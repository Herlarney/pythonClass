thislist = ["apple", "banana", "cherry"]
print(len(thislist))
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

list1 = ["abc", 34, True, 40, "male",8,7]

print(list1)

print(f'The length of the list is: {len(list1)}')
# List Negative indexing i
# -1 index means the last item, -2 means the second last item etc.
print(list1[-1])

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range
print(list1[2:5]) # This will return the items from index 2 to index 4 (5 is not included)
# The search will start at index 2 (included) and end at index 5 (not included).
print(f'The range of indexes when the start is not specified and the end is 5 is: {list1[:6]}')
print(f'The range of indexes when the end is not specified and the end is 5 is: {list1[4:]}')
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Negative indexing means starting from the end of the list.

#This example returns the items from index -4 (included) to index -1 (excluded)

#Remember that the last item has the index -1,

# Check if "apple" is present in the list:

if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

  thislist [1]= "mango"
  print(f"Yes, the list has been changed to {thislist}")
  thislist[2:5] = ["watermelon", "grape", "pineapple"]
  print(f"Yes, the list has been changed to {thislist}")
  thislist.insert(2, "papaya")
  print(f"Yes, the list has  papaya inserted and been changed to {thislist}"),
  thislist.append("orange")
  print(f"Yes, the list has  orange appended and been changed to {thislist}")
# Extending a list is adding the element of another 
# list to the end of the current list. 
# The extend() method adds the specified list elements (or any iterable) to the end of the current list.
  mixedList=[1,2,4,'a','d',403,]
  listToExtend=[1,2,3,4,5,6]
  mixedList.extend(listToExtend)
  print(f"Yes, the list has  been extended and changed to {mixedList}"),
  thistuple = ("kiwi", "orange")

  thislist.extend(thistuple)
  print(f"Yes, the list has  been extended and changed to {thislist}")
  thislist = ["apple", "banana", "cherry","plantain", "orange", "kiwi", "mango"]

  thislist.remove("banana")
  print(thislist)
  thislist.pop(3)
  print(f"the list has  been popped and changed to {thislist}")
#   If you do not specify the index, the pop() method removes the last item.

  thislist.pop()
  print(thislist)
     
        # LOOPING THROUGH A LIST
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
# Loop Through the Index Numbers
# You can also loop through the list items by referring to their index number.

# Use the range() and len() functions to create a suitable iterable.
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
  thislist1 = ["apple", "banana", "cherry","grape", "orange", "kiwi", "mango"]
i = 1
while i < len(thislist1):
  print(f"the while loop prints when i is {i}: {thislist1[i]}")
  i = i + 1
molecules = ["polyethylene", "nylon", "PVC", "polystyrene", "rubber","polyester", "polycarbonate", "polypropylene"]

# Print the first molecule
print(molecules[0])

# Print the last molecule
print(molecules[-1])

# Add a new molecule
molecules.append("kevlar")

# Print all molecules
for molecule in molecules:
    print(molecule)

  # List Comprehension
  # List comprehension offers a shorter syntax when you want to create a new list based on the
moleculesWhole = ["nylon", "polystyrene", "rubber","polyester", "polycarbonate", "polypropylene"]
newMolecule = []
for y in moleculesWhole:
   if "ny" in y:
      newMolecule.append(y)
print(f"The new molecule list is: {newMolecule}")

# Other usage of List Comprehension
num=[1,2,3,4,5,6,7,8,9,10.4,11.5,12.6,13.7,14.8,15.9]
newNum=[]
for x in num:
   if isinstance(x,float):
      newNum.append(x)
print(f"all the float numbers in the list are: {newNum}"),
# It can also be shorthanded to
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# Sort List
