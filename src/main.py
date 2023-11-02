
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# As of Python version 3.7, dictionaries are ordered. When we say that dictionaries are ordered,
# it means that the items have a defined order, and that order will not change.

thisDict = {'brand': 'Ford', 'model': 'Mustang', 'year': '1964'}

print(thisDict)
print(thisDict['brand'])

# Duplicate values will overwrite existing values:
thisDict2 = {'brand': 'Ford', 'model': 'Mustang', 'year': '1964', 'year': '2020'}
print(thisDict2)

print(len(thisDict))
print(len(thisDict2))

# The values in dictionary items can be of any data type:
thisDict3 = {'brand': 'Ford', 'electric': False, 'year': '1964', 'colors': ['red', 'white', 'blue']}
print(thisDict3)
print(thisDict3['colors'][1])

# From Python's perspective, dictionaries are defined as objects with the data type 'dict':
# <class 'dict'>
print(type(thisDict))

print(type(thisDict['brand']))

# It is also possible to use the dict() constructor to make a dictionary.
thisDict4 = dict(name='John', age=36, country='Norway')
print(thisDict4)


# https://www.w3schools.com/python/ref_func_open.asp

