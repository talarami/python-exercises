# For loop:

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I like {fruit}s")

# Output:
# I like apples
# I like bananas
# I like cherries

# While loop:

count = 0

while count < 5:
    print(f"Count is {count}")
    count += 1

# Output:
# Count is 0
# Count is 1
# Count is 2
# Count is 3
# Count is 4

# Using break:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num == 5:
        break
    print(num)

# Output:
# 1
# 2
# 3
# 4

# Using continue:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        continue
    print(num)

# Output:
# 1
# 3
# 5
# 7
# 9
