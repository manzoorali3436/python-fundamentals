"""
Python Tuple Packing and Unpacking

Definition:

Packing:
Packing means storing multiple values into a single tuple.

Example:
person = ("Ali", 25, "Developer")

Unpacking:
Unpacking means assigning the values of a tuple
to multiple variables.

Example:
name, age, job = person
"""

# =====================================================
# Example 1
# =====================================================
# Packing values into a tuple.

print("Example 1")

person = ("Ali", 25, "Developer")

print(person)

print("-" * 50)

# =====================================================
# Example 2
# =====================================================
# Unpacking a tuple.

print("Example 2")

person = ("Ali", 25, "Developer")

name, age, job = person

print(name)
print(age)
print(job)

print("-" * 50)

# =====================================================
# Example 3
# =====================================================
# Unpacking numbers.

print("Example 3")

numbers = (10, 20, 30)

first, second, third = numbers

print(first)
print(second)
print(third)

print("-" * 50)

# =====================================================
# Example 4
# =====================================================
# Unpacking colors.

print("Example 4")

colors = ("Red", "Blue", "Green")

color1, color2, color3 = colors

print(color1)
print(color2)
print(color3)

print("-" * 50)

# =====================================================
# Example 5
# =====================================================
# Variable names can be anything.

print("Example 5")

student = ("Ahmed", 18)

student_name, student_age = student

print(student_name)
print(student_age)

print("-" * 50)

# =====================================================
# Example 6
# =====================================================
# Number of variables must match.

print("Example 6")

fruits = ("Apple", "Banana", "Orange")

print(fruits)

# first, second = fruits

print("The number of variables must match the number of values.")

print("-" * 50)

# =====================================================
# Example 7
# =====================================================
# Ignore a value using _

print("Example 7")

person = ("Ali", 25, "Developer")

name, _, job = person

print(name)
print(job)

print("-" * 50)

# =====================================================
# Example 8
# =====================================================
# Swap two variables.

print("Example 8")

first = 10
second = 20

print("Before:", first, second)

first, second = second, first

print("After :", first, second)

print("-" * 50)

# =====================================================
# Example 9
# =====================================================
# User input.

print("Example 9")

first = input("Enter your first name: ")
last = input("Enter your last name: ")

person = (first, last)

first_name, last_name = person

print(first_name)
print(last_name)

print("-" * 50)

# =====================================================
# Example 10
# =====================================================
# Packing different data types.

print("Example 10")

data = ("Python", 3.14, True)

print(data)

print("-" * 50)

# =====================================================
# Example 11
# =====================================================
# Unpacking mixed values.

print("Example 11")

data = ("Python", 3.14, True)

language, version, available = data

print(language)
print(version)
print(available)

print("-" * 50)

# =====================================================
# Example 12
# =====================================================
# Packing game information.

print("Example 12")

game = ("Football", 11, True)

print(game)

print("-" * 50)

# =====================================================
# Example 13
# =====================================================
# Unpacking game information.

print("Example 13")

game = ("Football", 11, True)

name, players, outdoor = game

print(name)
print(players)
print(outdoor)

print("-" * 50)

# =====================================================
# Example 14
# =====================================================
# Unpacking marks.

print("Example 14")

marks = (85, 90, 95)

math, english, science = marks

print(math)
print(english)
print(science)

print("-" * 50)

# =====================================================
# Example 15
# =====================================================
# Packing user information.

print("Example 15")

user = ("Sara", 20, "Pakistan")

print(user)

print("-" * 50)

# =====================================================
# Example 16
# =====================================================
# Extended unpacking using *

print("Example 16")

numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print(first)
print(middle)
print(last)

print("-" * 50)

# =====================================================
# Example 17
# =====================================================
# * at the beginning.

print("Example 17")

numbers = (10, 20, 30, 40)

*start, last = numbers

print(start)
print(last)

print("-" * 50)

# =====================================================
# Example 18
# =====================================================
# * at the end.

print("Example 18")

numbers = (10, 20, 30, 40)

first, *rest = numbers

print(first)
print(rest)

print("-" * 50)

# =====================================================
# Example 19
# =====================================================
# Unpacking inside a loop.

print("Example 19")

students = (
    ("Ali", 20),
    ("Sara", 19),
    ("Ahmed", 21)
)

for name, age in students:
    print(name, "-", age)

print("-" * 50)

# =====================================================
# Example 20
# =====================================================
# Review.

print("Example 20")

person = ("Ali", 25, "Developer")

name, age, job = person

print("Name :", name)
print("Age  :", age)
print("Job  :", job)

print("-" * 50)

# =====================================================
# Summary
# =====================================================

print("Summary")

print("Packing stores multiple values in one tuple.")
print("Unpacking assigns tuple values to variables.")
print("The number of variables must match the number of values.")
print("Use _ to ignore values you don't need.")
print("Use * to collect multiple values into a list.")
print("Python can swap variables without a temporary variable.")