#print ('My name', 26, 'Is Adebayo') 

import random


x=3
y='my name is never Sikiru'
#print(x, y)
#print(y)
print("sikiru" in y)

# for x in 'banana':
#     print(x)
# slicing a string 
b = 'banana'
print(b[1:3])
print(b[1:]) # from index 1 to the end
print(b[:3]) # from the start to index 3

# NEGATIVE INDEXING, Stripping, Replacing, Uppercase and Lowercase, Splitting
b = "Hello, World!"
print(b[-3:-1])
print(b.upper())
c= "Hi, Ridwan!, heard you are a good programmer. "

print(c.strip())
print(c.replace("Ridwan", "Sikiru Ridwan Adebayo"))
print(c.split(","))

print("Learning Git!")

# f-String
age = 26
dob0 = 1997
txt = f"I am {age} and My name is Adebayo. I was born in {dob0}."
print(txt)


#  Walrus operator 
# Python 3.8 introduced the := operator, known as the "walrus operator". It assigns values to variables as part of a larger expression:
# e.g 
number = [1, 2, 3, 4, 5]
if (n := len(number)) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")

# Ternary operator
age = 17
status = "Adult" if age >= 18 else "Minor"
print(status)
# Membership operator
fruits = ["apple", "banana", "cherry"]
if "orange" in fruits:
    print("Orange is in the list")
else: 
    print("Orange is not in the list")
if "orange" not in fruits:
    print("Orange is not in the list")
    print("pineapple" not in fruits)

#     Inside the editor, complete the following steps:
# Create two variables a = 15 and b = 4
# Print the result of a modulus b (the % operator)
# Print the result of a floor division b (the // operator)
# Print the result of a to the power of b (the ** operator)
# Use an assignment operator to add 10 to a (use +=)
# Create variables
a=15
b=4
# Print modulus
print(a%b)
# Print floor division
print(a//b)
# Print power
print(a**b)
# Add 10 to a
a+=10
print(a)
