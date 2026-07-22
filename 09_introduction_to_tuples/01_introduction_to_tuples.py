"""
Python Tuples

Definition:
A tuple is a collection of multiple values stored
in a single variable.

Tuples are:
- Ordered
- Immutable (Cannot be changed)
- Allow duplicate values

Tuples are created using parentheses ().

Example:

fruits = ("Apple", "Banana", "Orange")
"""

# =====================================================
# Example 1
# =====================================================
# Creating a tuple.

print("Example 1")

fruits = ("Apple", "Banana", "Orange")

print(fruits)

print("-" * 50)

# =====================================================
# Example 2
# =====================================================
# Tuple of numbers.

print("Example 2")

numbers = (10, 20, 30, 40, 50)

print(numbers)

print("-" * 50)

# =====================================================
# Example 3
# =====================================================
# Tuple of strings.

print("Example 3")

students = ("Ali", "Ahmed", "Sara", "John")

print(students)

print("-" * 50)

# =====================================================
# Example 4
# =====================================================
# Tuple of boolean values.

print("Example 4")

results = (True, False, True)

print(results)

print("-" * 50)

# =====================================================
# Example 5
# =====================================================
# Mixed data types.

print("Example 5")

data = ("Ali", 20, True, 75.5)

print(data)

print("-" * 50)

# =====================================================
# Example 6
# =====================================================
# A tuple with one item.

print("Example 6")

fruit = ("Apple",)

print(fruit)

print(type(fruit))

print("-" * 50)

# =====================================================
# Example 7
# =====================================================
# This is NOT a tuple.

print("Example 7")

fruit = ("Apple")

print(fruit)

print(type(fruit))

print("-" * 50)

# =====================================================
# Example 8
# =====================================================
# Duplicate values.

print("Example 8")

colors = ("Red", "Blue", "Red", "Green")

print(colors)

print("-" * 50)

# =====================================================
# Example 9
# =====================================================
# Length of a tuple.

print("Example 9")

animals = ("Cat", "Dog", "Rabbit")

print(len(animals))

print("-" * 50)

# =====================================================
# Example 10
# =====================================================
# Type of a tuple.

print("Example 10")

countries = ("Pakistan", "Saudi Arabia", "Turkey")

print(type(countries))

print("-" * 50)

# =====================================================
# Example 11
# =====================================================
# Programming languages.

print("Example 11")

languages = (
    "Python",
    "PHP",
    "JavaScript"
)

print(languages)

print("-" * 50)

# =====================================================
# Example 12
# =====================================================
# School subjects.

print("Example 12")

subjects = (
    "Math",
    "English",
    "Science"
)

print(subjects)

print("-" * 50)

# =====================================================
# Example 13
# =====================================================
# Favorite foods.

print("Example 13")

foods = (
    "Pizza",
    "Burger",
    "Rice"
)

print(foods)

print("-" * 50)

# =====================================================
# Example 14
# =====================================================
# Weekdays.

print("Example 14")

days = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
)

print(days)

print("-" * 50)

# =====================================================
# Example 15
# =====================================================
# User input.

print("Example 15")

first = input("Enter first hobby: ")
second = input("Enter second hobby: ")
third = input("Enter third hobby: ")

hobbies = (first, second, third)

print(hobbies)

print("-" * 50)

# =====================================================
# Example 16
# =====================================================
# Tuple with floating-point numbers.

print("Example 16")

prices = (99.99, 150.50, 75.25)

print(prices)

print("-" * 50)

# =====================================================
# Example 17
# =====================================================
# Tuple with mixed values.

print("Example 17")

person = ("Ali", 25, "Developer", True)

print(person)

print("-" * 50)

# =====================================================
# Example 18
# =====================================================
# Empty tuple.

print("Example 18")

items = ()

print(items)

print(type(items))

print("-" * 50)

# =====================================================
# Example 19
# =====================================================
# Tuples are immutable.

print("Example 19")

fruits = ("Apple", "Banana", "Orange")

# fruits[0] = "Mango"

print("Tuples cannot be changed after creation.")

print("-" * 50)

# =====================================================
# Example 20
# =====================================================
# Review.

print("Example 20")

books = (
    "Python Basics",
    "Learning Programming",
    "Data Science"
)

print(books)

print("-" * 50)

# =====================================================
# Summary
# =====================================================

print("Summary")

print("A tuple stores multiple values.")
print("Tuples are ordered.")
print("Tuples are immutable (cannot be changed).")
print("Tuples allow duplicate values.")
print("Tuples are created using parentheses ().")
print("A single-item tuple needs a trailing comma.")
print("Use len() to count the number of items.")