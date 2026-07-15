"""
Python Data Types

Definition:
A data type defines what kind of value a variable can store and
what operations can be performed on it.

Python Built-in Data Types:
1. Numeric Types
2. String
3. List
4. Tuple
5. Set
6. Dictionary
7. Boolean
8. None
"""

# =====================================================
# Numeric Types
# =====================================================
# Definition:
# Numeric types are used to store numbers.
#
# Types:
# int     -> Whole numbers
# float   -> Decimal numbers
# complex -> Numbers with a real and imaginary part

integer_number = 25
float_number = 10.75
complex_number = 3 + 4j

print("Integer :", integer_number, type(integer_number))
print("Float   :", float_number, type(float_number))
print("Complex :", complex_number, type(complex_number))

print("-" * 50)

# =====================================================
# String (str)
# =====================================================
# Definition:
# A string is a sequence of characters enclosed in
# single quotes ('') or double quotes ("").

name = "Manzoor Ali"

print("String :", name)
print("Length :", len(name))
print("Upper  :", name.upper())
print("Lower  :", name.lower())

print("-" * 50)

# =====================================================
# List
# =====================================================
# Definition:
# A list is an ordered and mutable collection.
#
# Features:
# ✔ Ordered
# ✔ Changeable (Mutable)
# ✔ Allows duplicate values

fruits = ["Apple", "Banana", "Mango"]

fruits.append("Orange")

print("List :", fruits)

print("-" * 50)

# =====================================================
# Tuple
# =====================================================
# Definition:
# A tuple is an ordered but immutable collection.
#
# Features:
# ✔ Ordered
# ✔ Cannot be modified after creation
# ✔ Allows duplicate values

colors = ("Red", "Green", "Blue")

print("Tuple :", colors)

print("-" * 50)

# =====================================================
# Set
# =====================================================
# Definition:
# A set is an unordered collection of unique values.
#
# Features:
# ✔ Unordered
# ✔ Mutable
# ✔ Does NOT allow duplicates

numbers = {1, 2, 3, 3, 4, 5}

numbers.add(6)

print("Set :", numbers)

print("-" * 50)

# =====================================================
# Dictionary
# =====================================================
# Definition:
# A dictionary stores data as key-value pairs.
#
# Features:
# ✔ Keys are unique
# ✔ Mutable
# ✔ Fast data lookup

employee = {
    "name": "Manzoor",
    "age": 27,
    "country": "Pakistan"
}

print("Dictionary :", employee)
print("Employee Name :", employee["name"])

print("-" * 50)

# =====================================================
# Boolean
# =====================================================
# Definition:
# A Boolean represents one of two values:
# True or False.
#
# Commonly used in conditions and comparisons.

is_logged_in = True
is_admin = False

print("Boolean :", is_logged_in)
print("Boolean :", is_admin)

print("-" * 50)

# =====================================================
# None
# =====================================================
# Definition:
# None represents the absence of a value.
# It is often used as a placeholder.

result = None

print("None :", result)
print("Type :", type(result))

print("-" * 50)

# =====================================================
# Type Conversion
# =====================================================
# Definition:
# Type conversion changes one data type into another.

age = "25"

converted_age = int(age)

print("Original :", age, type(age))
print("Converted:", converted_age, type(converted_age))

print("-" * 50)

# =====================================================
# Checking a Data Type
# =====================================================
# Use type() to find the data type.
# Use isinstance() to check if an object belongs
# to a specific data type.

print(type(integer_number))
print(type(name))

print(isinstance(integer_number, int))
print(isinstance(name, str))
print(isinstance(fruits, list))