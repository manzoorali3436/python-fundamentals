"""
Python Nested Tuples

Definition:
A nested tuple is a tuple that contains one or more
tuples inside it.

Think of it like a table.

Example:

students = (
    ("Ali", 20),
    ("Sara", 19),
    ("Ahmed", 21)
)

Each inner tuple represents one row.
"""

# =====================================================
# Example 1
# =====================================================
# Creating a nested tuple.

print("Example 1")

students = (
    ("Ali", 20),
    ("Sara", 19),
    ("Ahmed", 21)
)

print(students)

print("-" * 50)

# =====================================================
# Example 2
# =====================================================
# Access the first row.

print("Example 2")

students = (
    ("Ali", 20),
    ("Sara", 19),
    ("Ahmed", 21)
)

print(students[0])

print("-" * 50)

# =====================================================
# Example 3
# =====================================================
# Access the second row.

print("Example 3")

students = (
    ("Ali", 20),
    ("Sara", 19),
    ("Ahmed", 21)
)

print(students[1])

print("-" * 50)

# =====================================================
# Example 4
# =====================================================
# Access a single value.

print("Example 4")

students = (
    ("Ali", 20),
    ("Sara", 19),
    ("Ahmed", 21)
)

print(students[0][0])

print("-" * 50)

# =====================================================
# Example 5
# =====================================================
# Access another value.

print("Example 5")

students = (
    ("Ali", 20),
    ("Sara", 19),
    ("Ahmed", 21)
)

print(students[1][1])

print("-" * 50)

# =====================================================
# Example 6
# =====================================================
# Access the last student's name.

print("Example 6")

students = (
    ("Ali", 20),
    ("Sara", 19),
    ("Ahmed", 21)
)

print(students[-1][0])

print("-" * 50)

# =====================================================
# Example 7
# =====================================================
# Print each row.

print("Example 7")

students = (
    ("Ali", 20),
    ("Sara", 19),
    ("Ahmed", 21)
)

for student in students:
    print(student)

print("-" * 50)

# =====================================================
# Example 8
# =====================================================
# Print each value.

print("Example 8")

students = (
    ("Ali", 20),
    ("Sara", 19),
    ("Ahmed", 21)
)

for student in students:
    for value in student:
        print(value)

print("-" * 50)

# =====================================================
# Example 9
# =====================================================
# Subjects and marks.

print("Example 9")

marks = (
    ("Math", 95),
    ("English", 88),
    ("Science", 91)
)

print(marks)

print("-" * 50)

# =====================================================
# Example 10
# =====================================================
# Print subjects and marks.

print("Example 10")

marks = (
    ("Math", 95),
    ("English", 88),
    ("Science", 91)
)

for subject in marks:
    print(subject[0], "-", subject[1])

print("-" * 50)

# =====================================================
# Example 11
# =====================================================
# Products.

print("Example 11")

products = (
    ("Laptop", 3500),
    ("Mouse", 80),
    ("Keyboard", 150)
)

print(products)

print("-" * 50)

# =====================================================
# Example 12
# =====================================================
# Print product names.

print("Example 12")

products = (
    ("Laptop", 3500),
    ("Mouse", 80),
    ("Keyboard", 150)
)

for product in products:
    print(product[0])

print("-" * 50)

# =====================================================
# Example 13
# =====================================================
# Days and temperatures.

print("Example 13")

weather = (
    ("Monday", 35),
    ("Tuesday", 36),
    ("Wednesday", 34)
)

for day in weather:
    print(day[0], "-", day[1], "°C")

print("-" * 50)

# =====================================================
# Example 14
# =====================================================
# Matrix.

print("Example 14")

matrix = (
    (1, 2),
    (3, 4)
)

print(matrix)

print("-" * 50)

# =====================================================
# Example 15
# =====================================================
# Print matrix values.

print("Example 15")

matrix = (
    (1, 2),
    (3, 4)
)

for row in matrix:
    for value in row:
        print(value)

print("-" * 50)

# =====================================================
# Example 16
# =====================================================
# User information.

print("Example 16")

users = (
    ("Ali", "Pakistan"),
    ("Sara", "Saudi Arabia")
)

for user in users:
    print(user[0], "-", user[1])

print("-" * 50)

# =====================================================
# Example 17
# =====================================================
# Classroom seating.

print("Example 17")

seats = (
    ("Ali", "Sara"),
    ("Ahmed", "John")
)

print(seats)

print("-" * 50)

# =====================================================
# Example 18
# =====================================================
# Employee information.

print("Example 18")

employees = (
    ("Ali", "Developer"),
    ("Sara", "Designer"),
    ("Ahmed", "Manager")
)

for employee in employees:
    print(employee[0], "-", employee[1])

print("-" * 50)

# =====================================================
# Example 19
# =====================================================
# Tuple unpacking with nested tuples.

print("Example 19")

students = (
    ("Ali", 20),
    ("Sara", 19),
    ("Ahmed", 21)
)

for name, age in students:
    print(name, "-", age)

print("-" * 50)

# =====================================================
# Example 20
# =====================================================
# Review.

print("Example 20")

books = (
    ("Python Basics", 250),
    ("Learn Programming", 300),
    ("AI Fundamentals", 450)
)

for title, price in books:
    print(title, "-", price)

print("-" * 50)

# =====================================================
# Summary
# =====================================================

print("Summary")

print("A nested tuple is a tuple inside another tuple.")
print("Use tuple[row][column] to access a value.")
print("Nested loops help you visit every value.")
print("You can unpack nested tuples in a for loop.")
print("Nested tuples are useful for storing structured data.")