```py
"""
All programs written in the class should start with a comment block such as

#Name
#Date
#Assignment

Example:

#Kyle Bennett
#Aug. 28, 2024
#Project 1

Output:
Use the print function
Syntax: print(params)
"""

print("Hello world")
print(24)

"""
Input: use the input() function
- syntax: input('path)
TIP: To save the input, you need to include the variable on the input() line
a variable is a named place in memory, without a variable the input will be lost
"""

# The name I enter will be stored in the name variable
name = input('Enter your name: ')
print('Your name is', name)

# If the input is a number, you need to wrap the input() with int()
# (everything from input() is a string by default)

age = int(input('Enter your age: '))
print('In 10 years you will be', age + 10, 'years old')
```