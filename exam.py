"""
1.
Convert this program into an equivalent list comprehension
students = ["Ana", "beth", "CHARLIE"] # keep this line
formatted_students = []
for student in students:
formatted_students.append(student.lower())
"""
students = ["Ana", "beth", "CHARLIE"] # keep this line
formatted_students = [student.lower() for student in students]

"""
2.
Given that input_str = “practice”, use string slicing to manipulate the
string so the output is “tap”.
"""
input_str = "practice"
input_str[::-1][3:8:2]

"""
Write code that reads in a file “input.txt” and for each line in the file
appends “...” on a new line
(Hint: first, figure out how many lines this file has)
"""
"""
lines = 0
with open("input.txt") as file:
    for line in file.readlines():
        lines += 1
with open("input.txt", "a") as file:
    for i in range(lines):
        file.write('\n...')

"""
"""
Write a function that takes in a dictionary representing a receipt of
items and their prices, and then returns the total price.
● The dictionary needs to be composed of at least 4 items
● Each item will have a key stating what the item is
● The value will be the price of the item as a float
● The total price is expected to be explicitly formatted
"""

receipt_dict = {
"TV": 1000.00,
"Mouse": 12.50,
"Screen Protector": 9.99,
"USB Stick": 4.99
}
def total_price(receipt):
    total = 0
    for k, v in receipt.items():
        total += v
    return round(total, 2)
print(total_price(receipt_dict))    