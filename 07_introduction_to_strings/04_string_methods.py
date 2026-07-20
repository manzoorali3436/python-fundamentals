"""
Python String Methods

Definition:
String methods are built-in functions that allow you
to perform different operations on strings.

Examples:
- Convert text to uppercase.
- Convert text to lowercase.
- Remove spaces.
- Replace words.
- Find text.
- Count characters.

Syntax:

string.method()
"""

# =====================================================
# Example 1
# =====================================================
# upper()

print("Example 1")

text = "hello python"

print(text.upper())

print("-" * 50)

# =====================================================
# Example 2
# =====================================================
# lower()

print("Example 2")

text = "HELLO PYTHON"

print(text.lower())

print("-" * 50)

# =====================================================
# Example 3
# =====================================================
# title()

print("Example 3")

text = "learning python is fun"

print(text.title())

print("-" * 50)

# =====================================================
# Example 4
# =====================================================
# capitalize()

print("Example 4")

text = "hello world"

print(text.capitalize())

print("-" * 50)

# =====================================================
# Example 5
# =====================================================
# strip()

print("Example 5")

text = "   Python   "

print(text.strip())

print("-" * 50)

# =====================================================
# Example 6
# =====================================================
# lstrip()

print("Example 6")

text = "   Python"

print(text.lstrip())

print("-" * 50)

# =====================================================
# Example 7
# =====================================================
# rstrip()

print("Example 7")

text = "Python   "

print(text.rstrip())

print("-" * 50)

# =====================================================
# Example 8
# =====================================================
# replace()

print("Example 8")

text = "I like Java"

print(text.replace("Java", "Python"))

print("-" * 50)

# =====================================================
# Example 9
# =====================================================
# find()

print("Example 9")

text = "Learning Python"

print(text.find("Python"))

print("-" * 50)

# =====================================================
# Example 10
# =====================================================
# count()

print("Example 10")

text = "banana"

print(text.count("a"))

print("-" * 50)

# =====================================================
# Example 11
# =====================================================
# startswith()

print("Example 11")

text = "Python Programming"

print(text.startswith("Python"))

print("-" * 50)

# =====================================================
# Example 12
# =====================================================
# endswith()

print("Example 12")

text = "photo.jpg"

print(text.endswith(".jpg"))

print("-" * 50)

# =====================================================
# Example 13
# =====================================================
# split()

print("Example 13")

text = "Apple Banana Orange"

print(text.split())

print("-" * 50)

# =====================================================
# Example 14
# =====================================================
# join()

print("Example 14")

words = ["Python", "is", "fun"]

print(" ".join(words))

print("-" * 50)

# =====================================================
# Example 15
# =====================================================
# isalpha()

print("Example 15")

text = "Python"

print(text.isalpha())

print("-" * 50)

# =====================================================
# Example 16
# =====================================================
# isdigit()

print("Example 16")

text = "12345"

print(text.isdigit())

print("-" * 50)

# =====================================================
# Example 17
# =====================================================
# isalnum()

print("Example 17")

text = "Python123"

print(text.isalnum())

print("-" * 50)

# =====================================================
# Example 18
# =====================================================
# islower()

print("Example 18")

text = "python"

print(text.islower())

print("-" * 50)

# =====================================================
# Example 19
# =====================================================
# isupper()

print("Example 19")

text = "PYTHON"

print(text.isupper())

print("-" * 50)

# =====================================================
# Example 20
# =====================================================
# swapcase()

print("Example 20")

text = "Python Programming"

print(text.swapcase())

print("-" * 50)

# =====================================================
# Summary
# =====================================================

print("Summary")

print("upper()       -> Converts to uppercase.")
print("lower()       -> Converts to lowercase.")
print("title()       -> Capitalizes each word.")
print("capitalize()  -> Capitalizes the first letter.")
print("strip()       -> Removes spaces from both sides.")
print("lstrip()      -> Removes spaces from the left.")
print("rstrip()      -> Removes spaces from the right.")
print("replace()     -> Replaces text.")
print("find()        -> Finds the position of text.")
print("count()       -> Counts occurrences.")
print("startswith()  -> Checks the beginning of text.")
print("endswith()    -> Checks the ending of text.")
print("split()       -> Splits text into a list.")
print("join()        -> Joins items into one string.")
print("isalpha()     -> Checks for letters only.")
print("isdigit()     -> Checks for digits only.")
print("isalnum()     -> Checks for letters and digits.")
print("islower()     -> Checks for lowercase.")
print("isupper()     -> Checks for uppercase.")
print("swapcase()    -> Swaps uppercase and lowercase.")