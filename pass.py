# The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

a = 33
b = 200

if b > a:
  pass
# Why Use pass?
# The pass statement is useful in several situations:

# When you're creating code structure but haven't implemented the logic yet
# When a statement is required syntactically but no action is needed
# As a placeholder for future code during development
# In empty functions or classes that you plan to implement later
value = 0

if value < 0:
  print("Negative value")
elif value == 0:
 pass # Zero case - no action needed
else:
  print("Positive value")


#   The Python Match Statement
# Instead of writing many if..else statements, you can use the match statement.

# The match statement selects one of many code blocks to be executed.
day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
#     Default Value
# Use the underscore character _ as the last case value if you want a code block to execute when there are not other matches:

day = 10
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")
    # Combine Values
# Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case:
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")
#     If Statements as Guards
# You can add if statements in the case evaluation as an extra condition-check:

month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")
#     Python Loop
i = 1
# while i < 6:
#   print(i)
#   i += 1
#    break Statement
# With the break statement we can stop the loop even if the while condition is true:i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#   The continue Statement
# With the continue statement we can stop the current iteration, and continue with the next:

# Example
# Continue to the next iteration if i is 3:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
#   The else Statement
# With the else statement we can run a block of code once when the condition no longer is true:

i = 6
while i < 12:
  print(i)
  i += 1
else:
  print("i is no longer less than 12")

#            FOR LOOP
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# Also use break statement to stop the loop before it has looped through all the items:
fruitList = ["apple", "banana", "cherry"]
for x in fruitList:
  print(x)
  if x == "banana":
    break
  
#   The range() Function
# To loop through a set of code a specified number of times, we can use the range() function,

# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for x in range(6):
  print(x)

# Using the start parameter:

for x in range(2, 6):
  print(f'this is number {x}')
# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
for x in range(2, 30, 3):
  print(x)
# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

# Print all numbers from 0 to 5, and print a message when the loop has ended:

for x in range(6):
  print(x)
else:
  print("Finally finished!")