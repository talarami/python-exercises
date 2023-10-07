"""
Create a program that tells you whether or not you need sunglasses when you leave
the house.
The program should:
1. Ask you if it is sunny using input()
2. If the input is 'y', it should output 'Take your sunglasses’
3. If the input is 'n', it should output 'You don't need sunglasses’
"""

weather = input("Is it sunny today? Please enter y for yes or n for no ")

if weather == "y":
    print("Take your sunglasses")   
elif weather == "n":
    print("You don't need sunglasses")
else:
    print("Invalid output. Please enter y for yes or n for no")