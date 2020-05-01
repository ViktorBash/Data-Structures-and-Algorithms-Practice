"""
Dictionaries are hash maps with keys and values.
There is not really ordering in dictionaries

Accessing a dictionary element is O(1) and efficient.
Accessing a list element is O(n) and still efficient, but not as efficient as accessing a dictionary.
"""

my_dict = {}
my_dict[1] = "Yes"
my_dict[0] = "No"

print(my_dict[1])


class my_class:
    def __init__(self):
        self.data = "data"


obj1 = my_class()
my_dict["object"] = obj1
print(my_dict["object"].data)
# Here we make a class with an object, and map that object to the dictionary. Then we can access attributes of the
# object from the dictionary

print(my_dict.keys())
# You cannot assume there will be ordering with dictionaries




