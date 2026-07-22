"""
Python Tuple Methods

Definition:
A tuple is immutable, which means its values cannot
be changed after it is created.

Because tuples cannot be modified, they have only
two built-in methods:

1. count()
2. index()

Built-in functions like len(), max(), min(), and sum()
also work with tuples.
"""

# =====================================================
# Example 1
# =====================================================
# count()
# Counts how many times a value appears.

print("Example 1")

numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))

print("-" * 50)

# =====================================================
# Example 2
# =====================================================
# Count duplicate strings.

print("Example 2")

fruits = ("Apple", "Banana", "Apple", "Orange")

print(fruits.count("Apple"))

print("-" * 50)

# =====================================================
# Example 3
# =====================================================
# Count boolean values.

print("Example 3")

results = (True, False, True, True)

print(results.count(True))

print("-" * 50)

# =====================================================
# Example 4
# =====================================================
# Count a value that doesn't exist.

print("Example 4")

numbers = (10, 20, 30)

print(numbers.count(100))

print("-" * 50)

# =====================================================
# Example 5
# =====================================================
# index()
# Finds the position of a value.

print("Example 5")

fruits = ("Apple", "Banana", "Orange")

print(fruits.index("Banana"))

print("-" * 50)

# =====================================================
# Example 6
# =====================================================
# index() returns the first match.

print("Example 6")

numbers = (10, 20, 10, 30)

print(numbers.index(10))

print("-" * 50)

# =====================================================
# Example 7
# =====================================================
# index() with strings.

print("Example 7")

colors = ("Red", "Blue", "Green")

print(colors.index("Green"))

print("-" * 50)

# =====================================================
# Example 8
# =====================================================
# Value not found.

print("Example 8")

animals = ("Cat", "Dog", "Rabbit")

# print(animals.index("Horse"))

print("Searching for a value that doesn't exist")
print("raises a ValueError.")

print("-" * 50)

# =====================================================
# Example 9
# =====================================================
# len()

print("Example 9")

students = ("Ali", "Sara", "Ahmed")

print(len(students))

print("-" * 50)

# =====================================================
# Example 10
# =====================================================
# max()

print("Example 10")

marks = (80, 95, 70, 90)

print(max(marks))

print("-" * 50)

# =====================================================
# Example 11
# =====================================================
# min()

print("Example 11")

marks = (80, 95, 70, 90)

print(min(marks))

print("-" * 50)

# =====================================================
# Example 12
# =====================================================
# sum()

print("Example 12")

numbers = (10, 20, 30, 40)

print(sum(numbers))

print("-" * 50)

# =====================================================
# Example 13
# =====================================================
# sorted()

print("Example 13")

numbers = (40, 10, 30, 20)

sorted_numbers = sorted(numbers)

print(sorted_numbers)

print(type(sorted_numbers))

print("-" * 50)

# =====================================================
# Example 14
# =====================================================
# tuple()

print("Example 14")

numbers = [1, 2, 3]

new_tuple = tuple(numbers)

print(new_tuple)

print(type(new_tuple))

print("-" * 50)

# =====================================================
# Example 15
# =====================================================
# User input.

print("Example 15")

first = input("Enter first fruit: ")
second = input("Enter second fruit: ")
third = input("Enter third fruit: ")

fruits = (first, second, third)

print(fruits.count(first))

print("-" * 50)

# =====================================================
# Example 16
# =====================================================
# Count letters.

print("Example 16")

letters = ("A", "B", "A", "C", "A")

print(letters.count("A"))

print("-" * 50)

# =====================================================
# Example 17
# =====================================================
# Find a month.

print("Example 17")

months = (
    "January",
    "February",
    "March",
    "April"
)

print(months.index("March"))

print("-" * 50)

# =====================================================
# Example 18
# =====================================================
# Count names.

print("Example 18")

names = (
    "Ali",
    "Sara",
    "Ali",
    "Ahmed"
)

print(names.count("Ali"))

print("-" * 50)

# =====================================================
# Example 19
# =====================================================
# Review.

print("Example 19")

languages = (
    "Python",
    "PHP",
    "Python",
    "JavaScript"
)

print(languages.count("Python"))
print(languages.index("PHP"))

print("-" * 50)

# =====================================================
# Example 20
# =====================================================
# Tuples cannot be modified.

print("Example 20")

fruits = ("Apple", "Banana", "Orange")

print(fruits)

# fruits.append("Mango")
# fruits.remove("Apple")

print("Tuples have no append(), remove(), or pop() methods.")

print("-" * 50)

# =====================================================
# Summary
# =====================================================

print("Summary")

print("count() -> Counts how many times a value appears.")
print("index() -> Finds the position of a value.")
print("Tuples cannot be modified.")
print("Tuples have only two built-in methods.")
print("Built-in functions like len(), max(), min(), sum(), and sorted() also work with tuples.")