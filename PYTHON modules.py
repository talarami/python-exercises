# 1. math module:

import math

result = math.sqrt(25)  # Calculate the square root of 25
print(result)  # Output: 5.0


# 2. random module:

import random

random_number = random.randint(1, 10)  # Generate a random integer between 1 and 10
print(random_number)


# 3. datetime module:

import datetime

current_time = datetime.datetime.now()
print(current_time)


# 4. json module:

import json

data = {"name": "Alice", "age": 30}
json_data = json.dumps(data)  # Convert a Python dictionary to a JSON string


# 5. requests module:

import requests

response = requests.get('https://www.example.com')
print(response.status_code)
