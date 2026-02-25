# ✅ FIXED VERSION — Python Bug Fixes

# Fix 1: Added missing colon after function def
# Cause: Python requires colon at end of 
# def, if, for, while statements
def greet(name):  # colon added
    print("Hello, " + name)

greet("Alex")

print("---")

# Fix 2: Correct indentation
# Cause: Python uses indentation to define 
# code blocks — inconsistent indent = error
def calculate_total(price, quantity):
    total = price * quantity  # indented correctly
    return total

print(calculate_total(10, 3))

print("---")

# Fix 3: Convert integer to string before concat
# Cause: Python cannot concatenate str and int
# directly unlike some other languages
age = 25
print("I am " + str(age) + " years old")
# Alternative cleaner fix using f-string:
print(f"I am {age} years old")

print("---")

# Fix 4: Python 3 handles division correctly
# This was an issue in Python 2 where int/int 
# returned int. In Python 3 it returns float.
# Added round() for clean output
def get_average(numbers):
    if len(numbers) == 0:
        return 0  # guard against empty list
    total = sum(numbers)
    count = len(numbers)
    return round(total / count, 2)

scores = [85, 90, 78]
print("Average:", get_average(scores))

print("---")

# Fix 5: Check index exists before accessing
# Cause: List has 3 items (index 0,1,2)
# Accessing index 3 throws IndexError
items = ["apple", "banana", "cherry"]

# Safe way 1: check length first
index = 3
if index < len(items):
    print(items[index])
else:
    print(f"Index {index} does not exist")

# Safe way 2: use try/except
try:
    print(items[3])
except IndexError:
    print("Item not found in list")

print("---")

# Fix 6: Use the correct variable name
# Cause: Variable defined as item_count 
# but referenced as total_items
def process_order():
    item_count = 5
    print("Processing " + str(item_count))
    # used item_count consistently

process_order()

print("---")

# Fix 7: Convert input to correct type
# Cause: input() always returns a string
# Comparing string "10" to integer 10 
# is always False
user_input = "10"  # simulating input for demo
if int(user_input) == 10:  # convert to int first
    print("You entered ten")

print("---")

# Fix 8: Always close files — use with statement
# Cause: Unclosed files cause memory leaks
# and can corrupt data
# Fix: with statement auto-closes file

def read_config():
    try:
        with open("config.txt", "r") as file:
            data = file.read()
            return data
    except FileNotFoundError:
        return "Config file not found"

print(read_config())
