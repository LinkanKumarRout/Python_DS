# Data Structure
# - A way to store and organize the data so that it can be accessed effectively.

# There are 2 types of data structure available.....
# Built-in
# - String, List, Tuple, Set, Dictionary, Bytearray

# User Defined
# Stack, Queue, Linked List, Tree, Graph, Matrix

# String Data Structure
'''
String is a collection of characters enclosed in quotes(single, double or tripple)
- String is immutable object

s = 'linkan'
print(s)

# All functions in a string
- len(), count(), index(), find(), upper(), lower(), isupper(), islower(), swapcase(), title(), capitalize(), startswith(), endswith(), split(), replace()
'''

# List Data Structure
'''
# List
- List is a collection of elements enclosed in a [].
- it can have different types of element.
- List is ordered. i.e [1,2,3,4,5] != [1,3,5,4,2]
- List element can be accessed using indexing. (0-based indexing)

lst = [12,3,24,54,34,33,22]
print(lst[0])

- list can be nested.
- list are mutable
- List are dynamic.

# All functions in a list
- sum(), max(), min(), all(), any(), append(), extend(), index(), remove(), pop(), len(), insert(), clear()
'''
# Tuple Data Structure
'''
- Tuple is a collection of elements enclosed is a ()
- it can be a collection of element separated with ,

- empty tuple like this -
a = tuple()
for a single element tuple you have to give a comma otherwise it will treat that variable based on the type()
a = (2,) if we don't give , it will be treated as an integer

- Tuples are immutable

# Creating a Tuple with
# the use of Strings
Tuple = ('Geeks', 'For')
print("\nTuple with the use of String: ")
print(Tuple)
    
# Creating a Tuple with
# the use of list
list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
Tuple = tuple(list1)

# Accessing element using indexing
print("First element of tuple")
print(Tuple[0])

# Accessing element from last
# negative indexing
print("\nLast element of tuple")
print(Tuple[-1])

print("\nThird last element of tuple")
print(Tuple[-3])

# All functions in tuple
- len(), sum(), max(), min(), index(), clear(), all(), any()
'''
# Set Data Structure
'''
Set is a cllection of unique and unordered elements enclosed by {}
- set does not support index no. bcz the insertion order in set is not fixed.
- set does not support concatenation and repeatation
-  sets are mutable that means we can add, delete data into/from our set
# Creating a Set with
# a mixed type of values
# (Having numbers and strings)
Set = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print("\nSet with the use of Mixed Values")
print(Set)

# Accessing element using
# for loop
print("\nElements of set: ")
for i in Set:
    print(i, end =" ")
print()

# Checking the element
# using in keyword
print("Geeks" in Set)

# All functions in a set
- len(), max(), min(), sum(), add(), remove(), discard(), all(), any(), clear()
- Some special functions like
- union(), intersection(), difference(), symmetric_difference(), intersection_update(), difference_update(), symmetric_difference_update()

# Frozen Set
- While set is mutable frozenset is immutable

s1 = frozenset([1,2,3,4])
s2 = frozenset([1,2,5,6])
print(s1.union(s2))

if we try to add or remove element from a frozenset it will give us Error
# s1.remove(1) # error
'''
# Dictionary Data Structure
'''
Python dictionary is an unordered collection of data that stores data in the format of key:value pair. It is like hash tables in any other language with the time complexity of O(1). Indexing of Python Dictionary is done with the help of keys. These are of any hashable type i.e. an object whose can never change like strings, numbers, tuples, etc. We can create a dictionary by using curly braces ({}) or dictionary comprehension.

# Creating a Dictionary
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("Creating Dictionary: ")
print(Dict)

# accessing a element using key
print("Accessing a element using key:")
print(Dict['Name'])

# accessing a element using get()
# method
print("Accessing a element using get:")
print(Dict.get(1))

# creation using Dictionary comprehension
myDict = {x: x**2 for x in [1,2,3,4,5]}
print(myDict)


# All functions in a dict
- pop(key), popitem(), keys(), values(), items(), update(), fromkeys()
'''
# Bytearray Data Structure
'''
Python Bytearray gives a mutable sequence of integers in the range 0 <= x < 256.

# Creating bytearray
a = bytearray((12, 8, 25, 2))
print("Creating Bytearray:")
print(a)

# accessing elements
print("\nAccessing Elements:", a[1])

# modifying elements
a[1] = 3
print("\nAfter Modifying:")
print(a)

# Appending elements
a.append(30)
print("\nAfter Adding Elements:")
print(a)
'''