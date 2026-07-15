"""
Python Input

Definition:
The input() function is used to receive data from the user through
the keyboard.

Important:
The value returned by input() is always a string (str), even if the
user enters a number.

Syntax:
input("Enter your value: ")
"""


# =====================================================
# f-String (Formatted String)
# =====================================================
# Definition:
# An f-string (formatted string literal) is a simple and readable
# way to insert variables or expressions directly inside a string.
#
# Syntax:
# f"Text {variable}"
#
# Note:
# Prefix the string with the letter 'f' and place variables
# or expressions inside curly braces {}.


# =====================================================
# Separator Line
# =====================================================
# Definition:
# The * operator repeats a string multiple times.
#
# In this example:
# "-" * 50 creates a string containing 50 hyphens.
#
# This is commonly used to separate sections of output
# and make the console easier to read.

print("-" * 50)


# =====================================================
# Basic Input
# =====================================================
# The input() function waits for the user to enter a value.


name = input("Enter your name: ")

print("Hello,", name)

print("-" * 50)

# =====================================================
# Multiple Inputs
# =====================================================
# You can ask the user for multiple values.

city = input("Enter your city: ")
country = input("Enter your country: ")

print(f"You live in {city}, {country}.")

print("-" * 50)

# =====================================================
# Numeric Input
# =====================================================
# Since input() always returns a string,
# convert it into an integer using int().

age = int(input("Enter your age: "))

print(f"You are {age} years old.")


print("-" * 50)

# =====================================================
# Float Input
# =====================================================
# Use float() for decimal numbers.

height = float(input("Enter your height (in meters): "))

print(f"Your height is {height} meters.")

print("-" * 50)

# =====================================================
# Performing Calculations
# =====================================================
# Convert inputs before performing arithmetic.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum_result = num1 + num2

print(f"Sum = {sum_result}")

print("-" * 50)

# =====================================================
# Taking Multiple Inputs on One Line
# =====================================================
# split() separates the input into multiple values.

first_name, last_name = input(
    "Enter your first and last name: "
).split()

print("First Name :", first_name)
print("Last Name  :", last_name)

print("-" * 50)

# =====================================================
# Multiple Numbers
# =====================================================
# map() applies int() to every value entered.

num1, num2, num3 = map(
    int,
    input("Enter three numbers separated by spaces: ").split()
)

print("Numbers :", num1, num2, num3)
print("Total   :", num1 + num2 + num3)

print("-" * 50)

# =====================================================
# Checking the Data Type
# =====================================================
# input() always returns a string unless converted.

user_input = input("Enter anything: ")

print("Value :", user_input)
print("Type  :", type(user_input))

print("-" * 50)

# =====================================================
# Summary
# =====================================================
# input() -> Returns a string
# int()   -> Converts to integer
# float() -> Converts to decimal number
# split() -> Splits one input into multiple values
# map()   -> Applies a function to multiple values