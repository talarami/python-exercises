import datetime
from datetime import datetime, date, timedelta

user_choice = input("Please select one of the following options: add, compare \n")

if user_choice == "add":
    user_date = datetime.strptime(input("What is the date you want to add to? Please enter in DD/MM/YYYY format. \n"), "%d/%m/%Y")
    print(user_date)
    user_days = int(input("How many days do you want to add? \n"))
    print(user_days)
    days_sum = user_date + timedelta(user_days)
    print("The resultant date is " + str(days_sum))
elif user_choice == "compare":
    user_date2 = datetime.strptime(input("Please give Date 1 in DD/MM/YYYY format. \n"), "%d/%m/%Y")
    print(user_date2.date())
    user_date3 = datetime.strptime(input("Please give Date 2 in DD/MM/YYYY format. \n"), "%d/%m/%Y")
    print(user_date3.date())
    delta = user_date2 - user_date3
    print("There are " + str(abs(delta.days)) + " days between the given dates")
else:
    "You need to choose add or compare"