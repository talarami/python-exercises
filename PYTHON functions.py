# Simple Function with Return:

def add(a, b):
    result = a + b
    return result

sum_result = add(3, 5)
print("Sum:", sum_result)  # Output: Sum: 8


# Function Returning Multiple Values (Tuple):

def divide_and_remainder(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

result = divide_and_remainder(20, 3)
print("Quotient:", result[0])  # Output: Quotient: 6
print("Remainder:", result[1])  # Output: Remainder: 2


# Function Returning Conditional Result:

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

result = is_even(7)
print("Is 7 even?", result)  # Output: Is 7 even? False


