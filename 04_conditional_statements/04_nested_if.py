"""
Python Nested if Statement

Definition:
A nested if statement is an if statement inside another
if statement.

The inner if statement is checked only if the outer
if condition is True.

Syntax:

if condition1:

    if condition2:
        # Executes when both conditions are True
"""

# =====================================================
# Example 1
# =====================================================
# Check if a person can vote.

print("Example 1")

age = 20
has_id_card = True

if age >= 18:
    print("You are an adult.")

    if has_id_card:
        print("You can vote.")
else:
    print("You are too young to vote.")

print("-" * 50)

# =====================================================
# Example 2
# =====================================================
# Buying a movie ticket.

print("Example 2")

has_money = True
ticket_available = True

if has_money:
    print("You have enough money.")

    if ticket_available:
        print("You bought the movie ticket.")
else:
    print("You need more money.")

print("-" * 50)

# =====================================================
# Example 3
# =====================================================
# Going to the park.

print("Example 3")

is_sunny = True
has_bicycle = False

if is_sunny:
    print("The weather is nice.")

    if has_bicycle:
        print("Let's ride the bicycle.")
    else:
        print("Let's go for a walk.")
else:
    print("Let's stay at home.")

print("-" * 50)

# =====================================================
# Example 4
# =====================================================
# Logging into a website.

print("Example 4")

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    print("Username is correct.")

    if password == "python123":
        print("Login successful!")
    else:
        print("Incorrect password.")
else:
    print("Username not found.")

print("-" * 50)

# =====================================================
# Example 5
# =====================================================
# Visiting a zoo.

print("Example 5")

has_ticket = True
age = 10

if has_ticket:
    print("Ticket verified.")

    if age < 12:
        print("Enjoy the children's area!")
    else:
        print("Enjoy all zoo attractions!")
else:
    print("Please buy a ticket first.")

print("-" * 50)

# =====================================================
# Example 6
# =====================================================
# Ice cream shop.

print("Example 6")

has_money = True
favorite_flavor = "Chocolate"

if has_money:
    print("You can buy an ice cream.")

    if favorite_flavor == "Chocolate":
        print("You bought a chocolate ice cream.")
    else:
        print("Choose another flavor.")
else:
    print("Save some money first.")

print("-" * 50)

# =====================================================
# Example 7
# =====================================================
# School admission.

print("Example 7")

age = 7
documents_complete = True

if age >= 5:
    print("Age requirement met.")

    if documents_complete:
        print("Admission approved.")
    else:
        print("Please submit the required documents.")
else:
    print("You are too young for admission.")

print("-" * 50)

# =====================================================
# Example 8
# =====================================================
# Playing a game.

print("Example 8")

game_installed = True
internet_connected = True

if game_installed:
    print("Game found.")

    if internet_connected:
        print("Starting online game...")
    else:
        print("Starting offline mode.")
else:
    print("Please install the game first.")

print("-" * 50)

# =====================================================
# Summary
# =====================================================

print("Summary")

print("✔ A nested if is an if statement inside another if.")
print("✔ The inner if is checked only when the outer if is True.")
print("✔ Nested if is useful when one decision depends on another.")
print("✔ It helps solve problems step by step.")