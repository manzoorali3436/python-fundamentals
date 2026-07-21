"""
Python List Methods

Definition:
List methods are built-in functions that help you
add, remove, search, sort, and copy items in a list.

Syntax:

list.method()
"""

# =====================================================
# Example 1
# =====================================================
# append()
# Adds one item to the end of the list.

print("Example 1")

fruits = ["Apple", "Banana"]

fruits.append("Orange")

print(fruits)

print("-" * 50)

# =====================================================
# Example 2
# =====================================================
# insert()
# Adds an item at a specific index.

print("Example 2")

fruits = ["Apple", "Orange"]

fruits.insert(1, "Banana")

print(fruits)

print("-" * 50)

# =====================================================
# Example 3
# =====================================================
# extend()
# Adds multiple items from another list.

print("Example 3")

fruits = ["Apple", "Banana"]
new_fruits = ["Orange", "Mango"]

fruits.extend(new_fruits)

print(fruits)

print("-" * 50)

# =====================================================
# Example 4
# =====================================================
# remove()
# Removes an item by its value.

print("Example 4")

fruits = ["Apple", "Banana", "Orange"]

fruits.remove("Banana")

print(fruits)

print("-" * 50)

# =====================================================
# Example 5
# =====================================================
# pop()
# Removes an item using its index.

print("Example 5")

numbers = [10, 20, 30, 40]

removed_number = numbers.pop(2)

print("Removed:", removed_number)
print(numbers)

print("-" * 50)

# =====================================================
# Example 6
# =====================================================
# pop()
# Removes the last item if no index is given.

print("Example 6")

colors = ["Red", "Blue", "Green"]

last_color = colors.pop()

print("Removed:", last_color)
print(colors)

print("-" * 50)

# =====================================================
# Example 7
# =====================================================
# clear()
# Removes all items from the list.

print("Example 7")

animals = ["Cat", "Dog", "Rabbit"]

animals.clear()

print(animals)

print("-" * 50)

# =====================================================
# Example 8
# =====================================================
# index()
# Finds the position of an item.

print("Example 8")

fruits = ["Apple", "Banana", "Orange"]

print(fruits.index("Banana"))

print("-" * 50)

# =====================================================
# Example 9
# =====================================================
# count()
# Counts how many times an item appears.

print("Example 9")

numbers = [10, 20, 10, 30, 10]

print(numbers.count(10))

print("-" * 50)

# =====================================================
# Example 10
# =====================================================
# sort()
# Sorts the list in ascending order.

print("Example 10")

numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)

print("-" * 50)

# =====================================================
# Example 11
# =====================================================
# sort(reverse=True)
# Sorts the list in descending order.

print("Example 11")

numbers = [40, 10, 30, 20]

numbers.sort(reverse=True)

print(numbers)

print("-" * 50)

# =====================================================
# Example 12
# =====================================================
# sort() with strings.

print("Example 12")

fruits = ["Orange", "Apple", "Banana"]

fruits.sort()

print(fruits)

print("-" * 50)

# =====================================================
# Example 13
# =====================================================
# reverse()
# Reverses the order of the list.

print("Example 13")

numbers = [1, 2, 3, 4, 5]

numbers.reverse()

print(numbers)

print("-" * 50)

# =====================================================
# Example 14
# =====================================================
# copy()
# Creates a copy of the list.

print("Example 14")

fruits = ["Apple", "Banana", "Orange"]

new_fruits = fruits.copy()

print(new_fruits)

print("-" * 50)

# =====================================================
# Example 15
# =====================================================
# len()
# Counts the number of items.

print("Example 15")

students = ["Ali", "Ahmed", "Sara"]

print(len(students))

print("-" * 50)

# =====================================================
# Example 16
# =====================================================
# max()

print("Example 16")

marks = [80, 95, 70, 90]

print(max(marks))

print("-" * 50)

# =====================================================
# Example 17
# =====================================================
# min()

print("Example 17")

marks = [80, 95, 70, 90]

print(min(marks))

print("-" * 50)

# =====================================================
# Example 18
# =====================================================
# sum()

print("Example 18")

numbers = [10, 20, 30, 40]

print(sum(numbers))

print("-" * 50)

# =====================================================
# Example 19
# =====================================================
# sorted()
# Returns a new sorted list.

print("Example 19")

numbers = [30, 10, 40, 20]

new_numbers = sorted(numbers)

print("Original:", numbers)
print("Sorted  :", new_numbers)

print("-" * 50)

# =====================================================
# Example 20
# =====================================================
# Review.

print("Example 20")

shopping = ["Milk", "Bread"]

shopping.append("Eggs")
shopping.insert(1, "Butter")
shopping.sort()

print(shopping)

print("-" * 50)

# =====================================================
# Summary
# =====================================================

print("Summary")

print("append()        -> Add one item.")
print("insert()        -> Add an item at a specific position.")
print("extend()        -> Add multiple items.")
print("remove()        -> Remove an item by value.")
print("pop()           -> Remove an item by index.")
print("clear()         -> Remove all items.")
print("index()         -> Find an item's index.")
print("count()         -> Count occurrences.")
print("sort()          -> Sort the list.")
print("reverse()       -> Reverse the list.")
print("copy()          -> Copy the list.")
print("len()           -> Count list items.")
print("max()           -> Largest value.")
print("min()           -> Smallest value.")
print("sum()           -> Total of numbers.")
print("sorted()        -> Return a sorted copy.")