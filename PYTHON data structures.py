# 1. Lists:

# Lists are ordered collections of elements.
# You can add, remove, or modify elements in a list.

# Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements
first_element = my_list[0]

# Modifying elements
my_list[1] = 10

# Adding elements
my_list.append(6)

# Removing elements
my_list.remove(3)

# Example
my_list = [1, 2, 3, 4, 5]
my_list.append(6)
my_list.remove(3)
print(my_list)  # Output: [1, 2, 4, 5, 6]


# 2. Tuples:

# Tuples are similar to lists but are immutable, meaning their elements cannot be changed after creation.

# Creating a tuple
my_tuple = (1, 2, 3)

# Accessing elements
first_element = my_tuple[0]

# Example
my_tuple = (1, 2, 3)
print(my_tuple[1])  # Output: 2


# 3. Dictionaries:

# Dictionaries store key-value pairs.
# You can add, modify, or delete key-value pairs.

# Creating a dictionary
my_dict = {'name': 'Alice', 'age': 30}

# Accessing values
name = my_dict['name']

# Modifying values
my_dict['age'] = 31

# Adding new key-value pairs
my_dict['city'] = 'New York'

# Removing key-value pairs
del my_dict['age']

# Example
my_dict = {'name': 'Alice', 'age': 30}
my_dict['city'] = 'New York'
del my_dict['age']
print(my_dict)  # Output: {'name': 'Alice', 'city': 'New York'}


# 4. Sets:

# Sets are unordered collections of unique elements.
# You can perform set operations like union, intersection, and difference.


# Creating a set
my_set = {1, 2, 3}

# Adding elements
my_set.add(4)

# Removing elements
my_set.remove(2)

# Example
my_set = {1, 2, 3}
my_set.add(4)
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4}


# 5. Strings:

# Strings are sequences of characters.
# You can manipulate strings using various string methods.

# Creating a string
my_string = "Hello, World!"

# Concatenation
new_string = my_string + " Welcome!"

# String methods
upper_case = my_string.upper() # upper case

length = len(my_string) # length

words = ["Hello", "World!"] # join words
sentence = " ".join(words)

text = "Hello, World!" # replace text
replaced_text = text.replace("World", "Python")






# Example
my_string = "Hello, World!"
new_string = my_string + " Welcome!"
upper_case = my_string.upper()
print(new_string)  # Output: Hello, World! Welcome!
print(upper_case)  # Output: HELLO, WORLD!
