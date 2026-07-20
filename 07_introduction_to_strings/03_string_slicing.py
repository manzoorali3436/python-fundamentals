"""
Python String Slicing

Definition:
String slicing allows you to extract a part of a string.

Syntax:

string[start:stop]

start:
The index where the slice begins.

stop:
The index where the slice ends.
The stop index is NOT included in the result.

You can also use:

string[start:stop:step]

step:
Specifies how many characters to skip.
"""

# =====================================================
# Example 1
# =====================================================
# Slice from index 0 to 3.

print("Example 1")

word = "Python"

print(word[0:3])

print("-" * 50)

# =====================================================
# Example 2
# =====================================================
# Slice from index 2 to 6.

print("Example 2")

word = "Python"

print(word[2:6])

print("-" * 50)

# =====================================================
# Example 3
# =====================================================
# Omit the start index.

print("Example 3")

word = "Python"

print(word[:4])

print("-" * 50)

# =====================================================
# Example 4
# =====================================================
# Omit the stop index.

print("Example 4")

word = "Python"

print(word[2:])

print("-" * 50)

# =====================================================
# Example 5
# =====================================================
# Copy the entire string.

print("Example 5")

word = "Python"

print(word[:])

print("-" * 50)

# =====================================================
# Example 6
# =====================================================
# Slice a person's name.

print("Example 6")

name = "Alexander"

print(name[0:5])

print("-" * 50)

# =====================================================
# Example 7
# =====================================================
# Slice a city name.

print("Example 7")

city = "Karachi"

print(city[3:])

print("-" * 50)

# =====================================================
# Example 8
# =====================================================
# Negative slicing.

print("Example 8")

word = "Python"

print(word[-3:])

print("-" * 50)

# =====================================================
# Example 9
# =====================================================
# Remove the first character.

print("Example 9")

word = "Python"

print(word[1:])

print("-" * 50)

# =====================================================
# Example 10
# =====================================================
# Remove the last character.

print("Example 10")

word = "Python"

print(word[:-1])

print("-" * 50)

# =====================================================
# Example 11
# =====================================================
# Every second character.

print("Example 11")

word = "Python"

print(word[::2])

print("-" * 50)

# =====================================================
# Example 12
# =====================================================
# Every third character.

print("Example 12")

word = "Programming"

print(word[::3])

print("-" * 50)

# =====================================================
# Example 13
# =====================================================
# Reverse a string.

print("Example 13")

word = "Python"

print(word[::-1])

print("-" * 50)

# =====================================================
# Example 14
# =====================================================
# Reverse a name.

print("Example 14")

name = "Ahmed"

print(name[::-1])

print("-" * 50)

# =====================================================
# Example 15
# =====================================================
# First three letters.

print("Example 15")

fruit = "Banana"

print(fruit[:3])

print("-" * 50)

# =====================================================
# Example 16
# =====================================================
# Last three letters.

print("Example 16")

fruit = "Banana"

print(fruit[-3:])

print("-" * 50)

# =====================================================
# Example 17
# =====================================================
# User input.

print("Example 17")

name = input("Enter your name: ")

print("First 3 letters:", name[:3])

print("-" * 50)

# =====================================================
# Example 18
# =====================================================
# Extract file extension.

print("Example 18")

filename = "photo.jpg"

print(filename[-3:])

print("-" * 50)

# =====================================================
# Example 19
# =====================================================
# Extract domain name.

print("Example 19")

email = "student@gmail.com"

print(email[8:])

print("-" * 50)

# =====================================================
# Example 20
# =====================================================
# Review.

print("Example 20")

language = "Python"

print("First  :", language[:2])
print("Middle :", language[2:4])
print("Last   :", language[-2:])

print("-" * 50)

# =====================================================
# Summary
# =====================================================

print("Summary")

print("string[start:stop]")
print("The stop index is NOT included.")
print("[:stop] starts from the beginning.")
print("[start:] goes to the end.")
print("[::step] skips characters.")
print("[::-1] reverses a string.")