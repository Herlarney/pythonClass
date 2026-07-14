# An "if statement" is written by using the if keyword.

a = 33
b = 200
if b > a:
  print("b is greater than a")

is_logged_in = True
if is_logged_in:
  print("Welcome back!")
#   Python can evaluate many types of values as True or False in an if statement.

# Zero (0), empty strings (""), None, and empty collections are treated as False. Everything else is treated as True.

# This includes positive numbers (5), negative numbers (-3), and any non-empty string (even "False" is treated as True because it's a non-empty string).
                                          # The Elif Keyword
# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

# The elif keyword allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True.

# Multiple elif statements can be used after an if statement to check multiple conditions.
score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")

  # Short Hand If...Else

  a = 5
b = 2
if a > b: print("a is greater than b")
# One-line if/else that prints a value:

c = 2
d= 330
print("A") if c > d else print("B")
# Multiple Conditions on One Line
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
# Multiple Nested If Statements
# Each if statement when fail print the else in the same indentation level as the if statement. The else statement is executed when the if statement fails.
score = 70
attendance = 75
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")