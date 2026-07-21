"""
Python List Comprehension

Definition:
A list comprehension is a short and easy way to create
a new list.

Instead of writing multiple lines with a for loop,
you can write everything in one line.

Syntax:

new_list = [expression for item in iterable]

You can also add a condition:

new_list = [expression for item in iterable if condition]
"""

# =====================================================
# Example 1
# =====================================================
# Create a list using a for loop.

print("Example 1")

numbers = []

for number in range(1, 6):
    numbers.append(number)

print(numbers)

print("-" * 50)

# =====================================================
# Example 2
# =====================================================
# Create the same list using list comprehension.

print("Example 2")

numbers = [number for number in range(1, 6)]

print(numbers)

print("-" * 50)

# =====================================================
# Example 3
# =====================================================
# Square each number.

print("Example 3")

squares = [number ** 2 for number in range(1, 6)]

print(squares)

print("-" * 50)

# =====================================================
# Example 4
# =====================================================
# Convert names to uppercase.

print("Example 4")

names = ["ali", "sara", "ahmed"]

uppercase_names = [name.upper() for name in names]

print(uppercase_names)

print("-" * 50)

# =====================================================
# Example 5
# =====================================================
# Get the length of each word.

print("Example 5")

words = ["Apple", "Banana", "Orange"]

lengths = [len(word) for word in words]

print(lengths)

print("-" * 50)

# =====================================================
# Example 6
# =====================================================
# Even numbers only.

print("Example 6")

even_numbers = [number for number in range(1, 11) if number % 2 == 0]

print(even_numbers)

print("-" * 50)

# =====================================================
# Example 7
# =====================================================
# Odd numbers only.

print("Example 7")

odd_numbers = [number for number in range(1, 11) if number % 2 != 0]

print(odd_numbers)

print("-" * 50)

# =====================================================
# Example 8
# =====================================================
# Numbers greater than 5.

print("Example 8")

numbers = [2, 4, 6, 8, 10]

greater_than_five = [number for number in numbers if number > 5]

print(greater_than_five)

print("-" * 50)

# =====================================================
# Example 9
# =====================================================
# First letter of each word.

print("Example 9")

fruits = ["Apple", "Banana", "Orange"]

first_letters = [fruit[0] for fruit in fruits]

print(first_letters)

print("-" * 50)

# =====================================================
# Example 10
# =====================================================
# Add 10 to every number.

print("Example 10")

numbers = [10, 20, 30]

new_numbers = [number + 10 for number in numbers]

print(new_numbers)

print("-" * 50)

# =====================================================
# Example 11
# =====================================================
# Multiply every number by 2.

print("Example 11")

numbers = [1, 2, 3, 4, 5]

doubled = [number * 2 for number in numbers]

print(doubled)

print("-" * 50)

# =====================================================
# Example 12
# =====================================================
# Remove spaces.

print("Example 12")

words = ["  Apple  ", " Banana ", " Orange "]

clean_words = [word.strip() for word in words]

print(clean_words)

print("-" * 50)

# =====================================================
# Example 13
# =====================================================
# Convert words to lowercase.

print("Example 13")

words = ["PYTHON", "PHP", "JAVASCRIPT"]

lowercase_words = [word.lower() for word in words]

print(lowercase_words)

print("-" * 50)

# =====================================================
# Example 14
# =====================================================
# Numbers divisible by 3.

print("Example 14")

numbers = [3, 5, 6, 9, 11, 12]

divisible_by_three = [
    number
    for number in numbers
    if number % 3 == 0
]

print(divisible_by_three)

print("-" * 50)

# =====================================================
# Example 15
# =====================================================
# User input.

print("Example 15")

first = input("Enter first fruit: ")
second = input("Enter second fruit: ")
third = input("Enter third fruit: ")

fruits = [first, second, third]

uppercase_fruits = [fruit.upper() for fruit in fruits]

print(uppercase_fruits)

print("-" * 50)

# =====================================================
# Example 16
# =====================================================
# Boolean values.

print("Example 16")

numbers = [2, 5, 8, 11]

results = [number > 5 for number in numbers]

print(results)

print("-" * 50)

# =====================================================
# Example 17
# =====================================================
# Add "Mr." before every name.

print("Example 17")

names = ["Ali", "Ahmed", "John"]

titles = [f"Mr. {name}" for name in names]

print(titles)

print("-" * 50)

# =====================================================
# Example 18
# =====================================================
# Copy a list.

print("Example 18")

colors = ["Red", "Blue", "Green"]

new_colors = [color for color in colors]

print(new_colors)

print("-" * 50)

# =====================================================
# Example 19
# =====================================================
# Numbers less than 50.

print("Example 19")

numbers = [25, 60, 45, 90, 15]

small_numbers = [number for number in numbers if number < 50]

print(small_numbers)

print("-" * 50)

# =====================================================
# Example 20
# =====================================================
# Review.

print("Example 20")

languages = ["Python", "PHP", "JavaScript"]

language_names = [language.upper() for language in languages]

print(language_names)

print("-" * 50)

# =====================================================
# Summary
# =====================================================

print("Summary")

print("List comprehension creates a new list.")
print("It is shorter than writing a for loop.")
print("You can transform items while creating a list.")
print("You can use conditions with if.")
print("It makes your code cleaner and easier to read.")