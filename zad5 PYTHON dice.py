"""
Write a program that simulates rolling two dice together 100 times. Record the
results of each roll to know how many 2s, 3s, 4s, 5s, 6s, 7s, 8s, 9s, 10s, 11s and 12s
were rolled. From this work out the probability of getting each number.
Tell the user they have two dice and ask them what number they are trying to get,
then return the probability of them getting that number.

For example:
● If 1 was the input, the output would be:
The chance of you getting 1 is 0%
● If 7 was the input, the output would be:
The chance of you getting 7 is 12%
"""

import random

"""
diceOne = random.randint(1, 6)
diceTwo = random.randint(1, 6)

print(diceOne)
print(diceTwo)

# dicesTogether = diceOne + diceTwo
# print(dicesTogether)

result = [random.randint(1, 6) + random.randint(1, 6) for i in range(100)]

print(result)

count_of_two = result.count(2)
print(count_of_two)

count_of_three = result.count(3)
print(count_of_three)

count_of_four = result.count(4)
print(count_of_four)

count_of_five = result.count(5)
print(count_of_five)

count_of_six = result.count(6)
print(count_of_six)

count_of_seven = result.count(7)
print(count_of_seven)

count_of_eight = result.count(8)
print(count_of_eight)

count_of_nine = result.count(9)
print(count_of_nine)

count_of_ten = result.count(10)
print(count_of_ten)

count_of_eleven = result.count(11)
print(count_of_eleven)

count_of_twelve = result.count(12)
print(count_of_twelve)

choosenNumber = input("Choose a number from 2 to 12: ")

if choosenNumber == "2":
    print("The chance of getting 2 is: " + str(count_of_two) + "%")

"""

listOfProbabilities = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(100):
    number = random.randint(1, 6) + random.randint(1, 6)
    listOfProbabilities[number-2] = listOfProbabilities[number-2] + 1

choosenNumber = input("Choose a number from 2 to 12: ")

print(listOfProbabilities)
print("you chose " + choosenNumber + ". It's probability is " + str(listOfProbabilities[int(choosenNumber)-2]) + "/100")



