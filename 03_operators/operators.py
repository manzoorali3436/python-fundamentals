"""
Python Operators

Definition:
Operators are special symbols used to perform operations on variables
and values.

Python Operators:
1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Identity Operators
6. Membership Operators
7. Bitwise Operators
"""

# =====================================================
# Arithmetic Operators
# =====================================================
# Definition:
# Arithmetic operators are used to perform mathematical operations.

number1 = 20
number2 = 10

print("Addition       :", number1 + number2)
print("Subtraction    :", number1 - number2)
print("Multiplication :", number1 * number2)
print("Division       :", number1 / number2)
print("Floor Division :", number1 // number2)
print("Modulus        :", number1 % number2)
print("Exponent       :", number1 ** 2)

print("-" * 50)

# =====================================================
# Assignment Operators
# =====================================================
# Definition:
# Assignment operators are used to assign or update values.

value = 10
print("Initial Value :", value)

value += 5
print("+= :", value)

value -= 3
print("-= :", value)

value *= 2
print("*= :", value)

value /= 4
print("/= :", value)

print("-" * 50)

# =====================================================
# Comparison Operators
# =====================================================
# Definition:
# Comparison operators compare two values and always return
# either True or False.

a = 15
b = 20

print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

print("-" * 50)

# =====================================================
# Logical Operators
# =====================================================
# Definition:
# Logical operators combine multiple conditions.

age = 25
has_license = True

print("AND :", age >= 18 and has_license)
print("OR  :", age >= 18 or False)
print("NOT :", not has_license)

print("-" * 50)

# =====================================================
# Identity Operators
# =====================================================
# Definition:
# Identity operators check whether two variables refer
# to the same object in memory.

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("list1 is list2     :", list1 is list2)
print("list1 is list3     :", list1 is list3)
print("list1 is not list3 :", list1 is not list3)

print("-" * 50)

# =====================================================
# Membership Operators
# =====================================================
# Definition:
# Membership operators check whether a value exists
# inside a sequence.

fruits = ["Apple", "Banana", "Orange"]

print("'Apple' in fruits     :", "Apple" in fruits)
print("'Mango' in fruits     :", "Mango" in fruits)
print("'Mango' not in fruits :", "Mango" not in fruits)

print("-" * 50)

# =====================================================
# Bitwise Operators
# =====================================================
# Definition:
# Bitwise operators work directly on the binary
# representation of integers.

x = 5
y = 3

print("AND (&) :", x & y)
print("OR (|)  :", x | y)
print("XOR (^) :", x ^ y)
print("NOT (~) :", ~x)
print("Left Shift (<<) :", x << 1)
print("Right Shift (>>) :", x >> 1)

print("-" * 50)

# =====================================================
# Summary
# =====================================================
# +   Addition
# -   Subtraction
# *   Multiplication
# /   Division
# //  Floor Division
# %   Modulus
# **  Exponent
#
# =   Assignment
# +=  Add and Assign
# -=  Subtract and Assign
#
# ==  Equal
# !=  Not Equal
# >   Greater Than
# <   Less Than
#
# and Logical AND
# or  Logical OR
# not Logical NOT
#
# is      Identity
# in      Membership
# & | ^   Bitwise Operators