# ❌ BROKEN VERSION — Common Python Bugs

# Bug 1: Syntax error — missing colon
def greet(name)
    print("Hello, " + name)

# Bug 2: Wrong indentation
def calculate_total(price, quantity):
total = price * quantity
    return total

# Bug 3: String and integer concatenation
age = 25
print("I am " + age + " years old")

# Bug 4: Division producing unexpected integer
def get_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total/count

scores = [85, 90, 78]
print(get_average(scores))

# Bug 5: List index out of range
items = ["apple", "banana", "cherry"]
print(items[3])

# Bug 6: Using undefined variable
def process_order():
    item_count = 5
    print("Processing " + str(total_items))

# Bug 7: Comparing wrong types
user_input = input("Enter a number: ")
if user_input == 10:
    print("You entered ten")

# Bug 8: File not closed after opening
def read_config():
    file = open("config.txt", "r")
    data = file.read()
    return data
