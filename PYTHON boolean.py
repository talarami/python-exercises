# Comparison Operators:
x = 5
y = 10

is_equal = x == y  # False
is_not_equal = x != y  # True
is_less_than = x < y  # True
is_greater_than_or_equal = x >= y  # False

# Logical Operators:
a = True
b = False

result_and = a and b  # False
result_or = a or b    # True
result_not_a = not a  # False

# Conditional Statements:
age = 25

if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# Functions and Boolean Return Values:
def is_even(number):
    return number % 2 == 0

print(is_even(4))  # True
print(is_even(7))  # False

# Boolean Expressions in Loops:
i = 0
while i < 5:
    print(i)
    i += 1

# Boolean as Flags:
user_logged_in = False

if user_logged_in:
    print("Welcome, user!")
else:
    print("Please log in to access the content.")
