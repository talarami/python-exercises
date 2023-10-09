"""
I have a list of students and I want to know after I sort the list, who is the first
student in alphabetical order.
students = [“Chloe”, “Anna”, “Lauren”, “Shreya”, “Siobhan”]
print(sorted(students)[1])
However, when I run the program it shows me a different answer to what I was
expecting? What is the mistake? How do I fix it?
"""

students = ["Chloe", "Anna", "Lauren", "Shreya", "Siobhan"]
            
print(sorted(students))

print(sorted(students)[0])

# Getting elements from list from the back:

elementList1 = ["Jan", "Tomek", "Beata", "Alicja"]

elementList1.reverse()
print(elementList1)