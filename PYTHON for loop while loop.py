# For loop:

# Here's an example that uses a for loop to iterate through a list of numbers and print each number:

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)


fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I like {fruit}s")

# Output:
# I like apples
# I like bananas
# I like cherries

# A while loop is used when you want to repeatedly execute a block of code 
# as long as a certain condition is true. Unlike the for loop, you might not know 
# in advance how many iterations will occur.

# While loop:

# Here's an example that uses a while loop to count from 0 to 4:

count = 0

while count < 5:
    print(f"Count is {count}")
    count += 1

# Here's an example that uses a while loop to count from 1 to 5:

count = 1
while count <= 5:
    print(count)
    count += 1


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

# Getting elements from list from the back using while:

elementList = ["Jan", "Tomek", "Beata", "Alicja"]
i = len(elementList) - 1

while i >= 0:
    person = elementList[i]
    print(person)
    i -= 1



