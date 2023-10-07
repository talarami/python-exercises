"""
You are trying to get rid of your old stuff in a bootsale and want to set up a program
to quickly return the price when given an item.
● Create a ‘shop’ dictionary with at least 4 items and respective prices.
● Write some code that will take in the name of an item and output the price
"""

shop = {
    "tshirt": 5,
    "jacket": 17,
    "skirt": 8,
    "jeans": 20,
    "dress": 12
}

print(shop["tshirt"])
print(shop["jacket"])
print("The price of dress is " + str(shop["dress"]))
