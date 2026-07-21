"""
Python Looping Through Lists

Definition:
Looping through a list means visiting each item in the
list one by one.

The most common way is to use a for loop.

Syntax:

for item in list:
    print(item)
"""

# =====================================================
# Example 1
# =====================================================
# Print all fruits.

print("Example 1")

fruits = ["Apple", "Banana", "Orange"]

for fruit in fruits:
    print(fruit)

print("-" * 50)

# =====================================================
# Example 2
# =====================================================
# Print all numbers.

print("Example 2")

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)

print("-" * 50)

# =====================================================
# Example 3
# =====================================================
# Print student names.

print("Example 3")

students = ["Ali", "Ahmed", "Sara"]

for student in students:
    print(student)

print("-" * 50)

# =====================================================
# Example 4
# =====================================================
# Print each color.

print("Example 4")

colors = ["Red", "Blue", "Green"]

for color in colors:
    print(color)

print("-" * 50)

# =====================================================
# Example 5
# =====================================================
# Print each item with a message.

print("Example 5")

animals = ["Cat", "Dog", "Rabbit"]

for animal in animals:
    print(f"I like {animal}")

print("-" * 50)

# =====================================================
# Example 6
# =====================================================
# Print each item in uppercase.

print("Example 6")

fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit.upper())

print("-" * 50)

# =====================================================
# Example 7
# =====================================================
# Count the total items.

print("Example 7")

games = ["Football", "Cricket", "Chess"]

count = 0

for game in games:
    count += 1

print("Total Games:", count)

print("-" * 50)

# =====================================================
# Example 8
# =====================================================
# Sum all numbers.

print("Example 8")

numbers = [10, 20, 30, 40]

total = 0

for number in numbers:
    total += number

print("Total:", total)

print("-" * 50)

# =====================================================
# Example 9
# =====================================================
# Find even numbers.

print("Example 9")

numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
    if number % 2 == 0:
        print(number)

print("-" * 50)

# =====================================================
# Example 10
# =====================================================
# Find odd numbers.

print("Example 10")

numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
    if number % 2 != 0:
        print(number)

print("-" * 50)

# =====================================================
# Example 11
# =====================================================
# Loop using indexes.

print("Example 11")

fruits = ["Apple", "Banana", "Orange"]

for index in range(len(fruits)):
    print(index, fruits[index])

print("-" * 50)

# =====================================================
# Example 12
# =====================================================
# While loop with a list.

print("Example 12")

fruits = ["Apple", "Banana", "Orange"]

index = 0

while index < len(fruits):
    print(fruits[index])
    index += 1

print("-" * 50)

# =====================================================
# Example 13
# =====================================================
# Skip an item using continue.

print("Example 13")

fruits = ["Apple", "Banana", "Orange"]

for fruit in fruits:
    if fruit == "Banana":
        continue

    print(fruit)

print("-" * 50)

# =====================================================
# Example 14
# =====================================================
# Stop the loop using break.

print("Example 14")

fruits = ["Apple", "Banana", "Orange", "Mango"]

for fruit in fruits:
    if fruit == "Orange":
        break

    print(fruit)

print("-" * 50)

# =====================================================
# Example 15
# =====================================================
# Print list items with numbers.

print("Example 15")

subjects = ["Math", "English", "Science"]

number = 1

for subject in subjects:
    print(f"{number}. {subject}")
    number += 1

print("-" * 50)

# =====================================================
# Example 16
# =====================================================
# User input.

print("Example 16")

first = input("Enter first hobby: ")
second = input("Enter second hobby: ")
third = input("Enter third hobby: ")

hobbies = [first, second, third]

for hobby in hobbies:
    print(hobby)

print("-" * 50)

# =====================================================
# Example 17
# =====================================================
# Find the largest number.

print("Example 17")

numbers = [25, 80, 15, 100, 40]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest:", largest)

print("-" * 50)

# =====================================================
# Example 18
# =====================================================
# Find the smallest number.

print("Example 18")

numbers = [25, 80, 15, 100, 40]

smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print("Smallest:", smallest)

print("-" * 50)

# =====================================================
# Example 19
# =====================================================
# Count vowels.

print("Example 19")

letters = ["a", "b", "e", "f", "i", "o", "u"]

count = 0

for letter in letters:
    if letter in ["a", "e", "i", "o", "u"]:
        count += 1

print("Vowels:", count)

print("-" * 50)

# =====================================================
# Example 20
# =====================================================
# Review.

print("Example 20")

languages = ["Python", "PHP", "JavaScript"]

for language in languages:
    print(f"I am learning {language}")

print("-" * 50)

# =====================================================
# Summary
# =====================================================

print("Summary")

print("Use a for loop to visit every item in a list.")
print("Use a while loop when you need an index.")
print("range(len(list)) gives both the index and the item.")
print("Use break to stop a loop early.")
print("Use continue to skip an item.")