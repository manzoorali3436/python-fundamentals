"""
Python Built-in Functions

Definition:
Built-in functions are functions that Python already
provides.

You can use them directly without creating your own
function.

Some commonly used built-in functions are:

print()
input()
type()
len()
sum()
max()
min()
abs()
round()
sorted()
int()
float()
str()
bool()
"""

# =====================================================
# Example 1
# =====================================================
# print()

print("Example 1")

print("Hello, Python!")

print("-" * 50)

# =====================================================
# Example 2
# =====================================================
# input()

print("Example 2")

name = input("Enter your name: ")

print("Welcome,", name)

print("-" * 50)

# =====================================================
# Example 3
# =====================================================
# type()

print("Example 3")

age = 25

print(type(age))

print(type("Python"))

print(type(True))

print("-" * 50)

# =====================================================
# Example 4
# =====================================================
# len()

print("Example 4")

name = "Python"

print("Length:", len(name))

print("-" * 50)

# =====================================================
# Example 5
# =====================================================
# len() with a list.

print("Example 5")

fruits = ["Apple", "Banana", "Orange"]

print("Total Fruits:", len(fruits))

print("-" * 50)

# =====================================================
# Example 6
# =====================================================
# sum()

print("Example 6")

numbers = [10, 20, 30, 40]

print("Sum:", sum(numbers))

print("-" * 50)

# =====================================================
# Example 7
# =====================================================
# max()

print("Example 7")

numbers = [15, 50, 8, 22]

print("Largest Number:", max(numbers))

print("-" * 50)

# =====================================================
# Example 8
# =====================================================
# min()

print("Example 8")

numbers = [15, 50, 8, 22]

print("Smallest Number:", min(numbers))

print("-" * 50)

# =====================================================
# Example 9
# =====================================================
# abs()

print("Example 9")

print(abs(-25))

print(abs(-99.5))

print("-" * 50)

# =====================================================
# Example 10
# =====================================================
# round()

print("Example 10")

print(round(3.14159, 2))

print(round(8.5678, 1))

print("-" * 50)

# =====================================================
# Example 11
# =====================================================
# sorted()

print("Example 11")

numbers = [8, 2, 10, 4, 1]

print(sorted(numbers))

print("-" * 50)

# =====================================================
# Example 12
# =====================================================
# int()

print("Example 12")

age = "25"

print(int(age))

print("-" * 50)

# =====================================================
# Example 13
# =====================================================
# float()

print("Example 13")

price = "99.95"

print(float(price))

print("-" * 50)

# =====================================================
# Example 14
# =====================================================
# str()

print("Example 14")

number = 100

print(str(number))

print(type(str(number)))

print("-" * 50)

# =====================================================
# Example 15
# =====================================================
# bool()

print("Example 15")

print(bool(1))

print(bool(0))

print(bool("Python"))

print(bool(""))

print("-" * 50)

# =====================================================
# Example 16
# =====================================================
# range()

print("Example 16")

print(list(range(1, 6)))

print("-" * 50)

# =====================================================
# Example 17
# =====================================================
# id()

print("Example 17")

name = "Python"

print(id(name))

print("-" * 50)

# =====================================================
# Example 18
# =====================================================
# pow()

print("Example 18")

print(pow(2, 3))

print(pow(5, 2))

print("-" * 50)

# =====================================================
# Example 19
# =====================================================
# divmod()

print("Example 19")

print(divmod(17, 5))

print("-" * 50)

# =====================================================
# Example 20
# =====================================================
# all() and any()

print("Example 20")

print(all([True, True, True]))

print(any([False, False, True]))

print("-" * 50)

# =====================================================
# Summary
# =====================================================

print("Summary")

print("print()   -> Display output.")
print("input()   -> Get user input.")
print("type()    -> Show the data type.")
print("len()     -> Count items.")
print("sum()     -> Add numbers.")
print("max()     -> Largest value.")
print("min()     -> Smallest value.")
print("abs()     -> Positive value.")
print("round()   -> Round a number.")
print("sorted()  -> Sort values.")
print("int()     -> Convert to integer.")
print("float()   -> Convert to float.")
print("str()     -> Convert to string.")
print("bool()    -> Convert to boolean.")
print("range()   -> Generate a sequence.")
print("id()      -> Show the object's unique ID.")
print("pow()     -> Raise a number to a power.")
print("divmod()  -> Return quotient and remainder.")
print("all()     -> True if all values are True.")
print("any()     -> True if at least one value is True.")