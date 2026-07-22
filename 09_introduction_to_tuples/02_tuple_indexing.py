"""
Python Tuple Indexing

Definition:
Tuple indexing allows you to access a single item
from a tuple using its position (index).

Python starts counting from 0.

Example:

fruits = ("Apple", "Banana", "Orange")

Item:   Apple   Banana   Orange
Index:     0        1        2

Negative indexing starts from the end.

Item:   Apple   Banana   Orange
Index:    -3      -2       -1
"""

# =====================================================
# Example 1
# =====================================================
# Access the first item.

print("Example 1")

fruits = ("Apple", "Banana", "Orange")

print(fruits[0])

print("-" * 50)

# =====================================================
# Example 2
# =====================================================
# Access the second item.

print("Example 2")

fruits = ("Apple", "Banana", "Orange")

print(fruits[1])

print("-" * 50)

# =====================================================
# Example 3
# =====================================================
# Access the last item.

print("Example 3")

fruits = ("Apple", "Banana", "Orange")

print(fruits[2])

print("-" * 50)

# =====================================================
# Example 4
# =====================================================
# Access the first item using a negative index.

print("Example 4")

fruits = ("Apple", "Banana", "Orange")

print(fruits[-3])

print("-" * 50)

# =====================================================
# Example 5
# =====================================================
# Access the last item using a negative index.

print("Example 5")

fruits = ("Apple", "Banana", "Orange")

print(fruits[-1])

print("-" * 50)

# =====================================================
# Example 6
# =====================================================
# Access student names.

print("Example 6")

students = ("Ali", "Ahmed", "Sara", "John")

print(students[0])
print(students[2])
print(students[-1])

print("-" * 50)

# =====================================================
# Example 7
# =====================================================
# Access numbers.

print("Example 7")

numbers = (10, 20, 30, 40, 50)

print(numbers[0])
print(numbers[3])
print(numbers[-2])

print("-" * 50)

# =====================================================
# Example 8
# =====================================================
# Access colors.

print("Example 8")

colors = ("Red", "Blue", "Green", "Black")

print(colors[1])
print(colors[-1])

print("-" * 50)

# =====================================================
# Example 9
# =====================================================
# User input.

print("Example 9")

first = input("Enter first fruit: ")
second = input("Enter second fruit: ")
third = input("Enter third fruit: ")

fruits = (first, second, third)

print("First Fruit:", fruits[0])

print("-" * 50)

# =====================================================
# Example 10
# =====================================================
# Access the last animal.

print("Example 10")

animals = ("Cat", "Dog", "Rabbit", "Horse")

print("Last Animal:", animals[-1])

print("-" * 50)

# =====================================================
# Example 11
# =====================================================
# Store an item in a variable.

print("Example 11")

cities = ("Karachi", "Lahore", "Islamabad")

city = cities[1]

print(city)

print("-" * 50)

# =====================================================
# Example 12
# =====================================================
# Access boolean values.

print("Example 12")

results = (True, False, True)

print(results[0])
print(results[1])

print("-" * 50)

# =====================================================
# Example 13
# =====================================================
# Access mixed data types.

print("Example 13")

data = ("Ali", 20, True, 90.5)

print(data[0])
print(data[1])
print(data[2])
print(data[3])

print("-" * 50)

# =====================================================
# Example 14
# =====================================================
# Tuples cannot be modified.

print("Example 14")

fruits = ("Apple", "Banana", "Orange")

print(fruits)

# fruits[1] = "Mango"

print("Tuples are immutable.")
print("You cannot change an item using its index.")

print("-" * 50)

# =====================================================
# Example 15
# =====================================================
# Index out of range.

print("Example 15")

languages = ("Python", "PHP", "JavaScript")

print(languages)

# print(languages[5])
# Uncommenting this line will cause:
# IndexError: tuple index out of range

print("Index must be within the tuple length.")

print("-" * 50)

# =====================================================
# Example 16
# =====================================================
# Loop using indexes.

print("Example 16")

fruits = ("Apple", "Banana", "Orange")

for index in range(len(fruits)):
    print(index, fruits[index])

print("-" * 50)

# =====================================================
# Example 17
# =====================================================
# Compare tuple items.

print("Example 17")

fruits = ("Apple", "Banana", "Orange")

print(fruits[0] == "Apple")
print(fruits[-1] == "Orange")

print("-" * 50)

# =====================================================
# Example 18
# =====================================================
# Access months.

print("Example 18")

months = (
    "January",
    "February",
    "March",
    "April"
)

print(months[2])

print("-" * 50)

# =====================================================
# Example 19
# =====================================================
# Access countries.

print("Example 19")

countries = (
    "Pakistan",
    "Saudi Arabia",
    "Turkey"
)

print(countries[-2])

print("-" * 50)

# =====================================================
# Example 20
# =====================================================
# Review.

print("Example 20")

subjects = (
    "Math",
    "English",
    "Science"
)

print("First :", subjects[0])
print("Second:", subjects[1])
print("Last  :", subjects[-1])

print("-" * 50)

# =====================================================
# Summary
# =====================================================

print("Summary")

print("Tuple indexing accesses one item from a tuple.")
print("Positive indexing starts from 0.")
print("Negative indexing starts from -1.")
print("Tuples are immutable.")
print("Using an invalid index causes an IndexError.")