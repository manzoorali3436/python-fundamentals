"""
Python String Indexing

Definition:
String indexing allows you to access a single character
from a string using its position (index).

Python starts counting from 0.

Example:

Word: Python

Character: P  y  t  h  o  n
Index:     0  1  2  3  4  5

Negative indexing starts from the end.

Character: P  y  t  h  o  n
Index:    -6 -5 -4 -3 -2 -1
"""

# =====================================================
# Example 1
# =====================================================
# First character.

print("Example 1")

word = "Python"

print(word[0])

print("-" * 50)

# =====================================================
# Example 2
# =====================================================
# Second character.

print("Example 2")

word = "Python"

print(word[1])

print("-" * 50)

# =====================================================
# Example 3
# =====================================================
# Last character using positive index.

print("Example 3")

word = "Python"

print(word[5])

print("-" * 50)

# =====================================================
# Example 4
# =====================================================
# First character using negative index.

print("Example 4")

word = "Python"

print(word[-6])

print("-" * 50)

# =====================================================
# Example 5
# =====================================================
# Last character using negative index.

print("Example 5")

word = "Python"

print(word[-1])

print("-" * 50)

# =====================================================
# Example 6
# =====================================================
# Access different characters.

print("Example 6")

name = "Ahmed"

print(name[0])
print(name[2])
print(name[4])

print("-" * 50)

# =====================================================
# Example 7
# =====================================================
# Access characters from a city name.

print("Example 7")

city = "Karachi"

print(city[0])
print(city[3])
print(city[-1])

print("-" * 50)

# =====================================================
# Example 8
# =====================================================
# Access characters from a country name.

print("Example 8")

country = "Pakistan"

print(country[0])
print(country[4])
print(country[-2])

print("-" * 50)

# =====================================================
# Example 9
# =====================================================
# User input.

print("Example 9")

name = input("Enter your name: ")

print("First Letter:", name[0])

print("-" * 50)

# =====================================================
# Example 10
# =====================================================
# Last letter from user input.

print("Example 10")

word = input("Enter a word: ")

print("Last Letter:", word[-1])

print("-" * 50)

# =====================================================
# Example 11
# =====================================================
# Middle character.

print("Example 11")

fruit = "Banana"

print(fruit[2])

print("-" * 50)

# =====================================================
# Example 12
# =====================================================
# School name.

print("Example 12")

school = "Sunrise School"

print(school[0])
print(school[8])

print("-" * 50)

# =====================================================
# Example 13
# =====================================================
# Email address.

print("Example 13")

email = "student@example.com"

print(email[0])
print(email[-1])

print("-" * 50)

# =====================================================
# Example 14
# =====================================================
# Phone number.

print("Example 14")

phone = "03001234567"

print(phone[0])
print(phone[-1])

print("-" * 50)

# =====================================================
# Example 15
# =====================================================
# Index Error.

print("Example 15")

language = "Python"

print(language)

# print(language[10])
# Uncommenting this line will cause:
# IndexError: string index out of range

print("Index must be within the string length.")

print("-" * 50)

# =====================================================
# Example 16
# =====================================================
# Loop through characters using indexing.

print("Example 16")

word = "Cat"

for index in range(len(word)):
    print(word[index])

print("-" * 50)

# =====================================================
# Example 17
# =====================================================
# Compare characters.

print("Example 17")

word = "Python"

print(word[0] == "P")
print(word[-1] == "n")

print("-" * 50)

# =====================================================
# Example 18
# =====================================================
# Store a character.

print("Example 18")

word = "Orange"

first_letter = word[0]

print(first_letter)

print("-" * 50)

# =====================================================
# Example 19
# =====================================================
# Favorite color.

print("Example 19")

color = "Blue"

print(color[1])

print("-" * 50)

# =====================================================
# Example 20
# =====================================================
# Review.

print("Example 20")

animal = "Elephant"

print("First :", animal[0])
print("Last  :", animal[-1])

print("-" * 50)

# =====================================================
# Summary
# =====================================================

print("Summary")

print("String indexing accesses one character.")
print("Positive indexing starts from 0.")
print("Negative indexing starts from -1.")
print("Use [] with an index to get a character.")
print("An invalid index causes an IndexError.")