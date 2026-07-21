"""
Python Nested Lists

Definition:
A nested list is a list that contains one or more lists
inside it.

Think of it like a table.

Example:

students = [
    ["Ali", 20],
    ["Sara", 19],
    ["Ahmed", 21]
]

Each inner list represents one row.
"""

# =====================================================
# Example 1
# =====================================================
# Creating a nested list.

print("Example 1")

students = [
    ["Ali", 20],
    ["Sara", 19],
    ["Ahmed", 21]
]

print(students)

print("-" * 50)

# =====================================================
# Example 2
# =====================================================
# Access the first row.

print("Example 2")

students = [
    ["Ali", 20],
    ["Sara", 19],
    ["Ahmed", 21]
]

print(students[0])

print("-" * 50)

# =====================================================
# Example 3
# =====================================================
# Access the second row.

print("Example 3")

students = [
    ["Ali", 20],
    ["Sara", 19],
    ["Ahmed", 21]
]

print(students[1])

print("-" * 50)

# =====================================================
# Example 4
# =====================================================
# Access a single value.

print("Example 4")

students = [
    ["Ali", 20],
    ["Sara", 19],
    ["Ahmed", 21]
]

print(students[0][0])

print("-" * 50)

# =====================================================
# Example 5
# =====================================================
# Access another value.

print("Example 5")

students = [
    ["Ali", 20],
    ["Sara", 19],
    ["Ahmed", 21]
]

print(students[1][1])

print("-" * 50)

# =====================================================
# Example 6
# =====================================================
# Access the last student's name.

print("Example 6")

students = [
    ["Ali", 20],
    ["Sara", 19],
    ["Ahmed", 21]
]

print(students[-1][0])

print("-" * 50)

# =====================================================
# Example 7
# =====================================================
# Change a value.

print("Example 7")

students = [
    ["Ali", 20],
    ["Sara", 19]
]

students[0][1] = 21

print(students)

print("-" * 50)

# =====================================================
# Example 8
# =====================================================
# Add a new row.

print("Example 8")

students = [
    ["Ali", 20],
    ["Sara", 19]
]

students.append(["John", 18])

print(students)

print("-" * 50)

# =====================================================
# Example 9
# =====================================================
# Loop through rows.

print("Example 9")

students = [
    ["Ali", 20],
    ["Sara", 19],
    ["Ahmed", 21]
]

for student in students:
    print(student)

print("-" * 50)

# =====================================================
# Example 10
# =====================================================
# Loop through each value.

print("Example 10")

students = [
    ["Ali", 20],
    ["Sara", 19],
    ["Ahmed", 21]
]

for student in students:
    for value in student:
        print(value)

print("-" * 50)

# =====================================================
# Example 11
# =====================================================
# Subjects and marks.

print("Example 11")

marks = [
    ["Math", 95],
    ["English", 88],
    ["Science", 91]
]

print(marks)

print("-" * 50)

# =====================================================
# Example 12
# =====================================================
# Print subjects and marks.

print("Example 12")

marks = [
    ["Math", 95],
    ["English", 88],
    ["Science", 91]
]

for subject in marks:
    print(subject[0], "-", subject[1])

print("-" * 50)

# =====================================================
# Example 13
# =====================================================
# Products.

print("Example 13")

products = [
    ["Laptop", 3500],
    ["Mouse", 80],
    ["Keyboard", 150]
]

print(products)

print("-" * 50)

# =====================================================
# Example 14
# =====================================================
# Print product names.

print("Example 14")

products = [
    ["Laptop", 3500],
    ["Mouse", 80],
    ["Keyboard", 150]
]

for product in products:
    print(product[0])

print("-" * 50)

# =====================================================
# Example 15
# =====================================================
# Days and temperatures.

print("Example 15")

weather = [
    ["Monday", 35],
    ["Tuesday", 36],
    ["Wednesday", 34]
]

for day in weather:
    print(day[0], "-", day[1], "°C")

print("-" * 50)

# =====================================================
# Example 16
# =====================================================
# Matrix.

print("Example 16")

matrix = [
    [1, 2],
    [3, 4]
]

print(matrix)

print("-" * 50)

# =====================================================
# Example 17
# =====================================================
# Print matrix values.

print("Example 17")

matrix = [
    [1, 2],
    [3, 4]
]

for row in matrix:
    for value in row:
        print(value)

print("-" * 50)

# =====================================================
# Example 18
# =====================================================
# User information.

print("Example 18")

users = [
    ["Ali", "Pakistan"],
    ["Sara", "Saudi Arabia"]
]

for user in users:
    print(user[0], "-", user[1])

print("-" * 50)

# =====================================================
# Example 19
# =====================================================
# Classroom seating.

print("Example 19")

seats = [
    ["Ali", "Sara"],
    ["Ahmed", "John"]
]

print(seats)

print("-" * 50)

# =====================================================
# Example 20
# =====================================================
# Review.

print("Example 20")

employees = [
    ["Ali", "Developer"],
    ["Sara", "Designer"],
    ["Ahmed", "Manager"]
]

for employee in employees:
    print(employee[0], "-", employee[1])

print("-" * 50)

# =====================================================
# Summary
# =====================================================

print("Summary")

print("A nested list is a list inside another list.")
print("Use list[row][column] to access a value.")
print("Nested loops are useful for nested lists.")
print("Nested lists can represent tables and matrices.")