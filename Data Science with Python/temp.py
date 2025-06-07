# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
x = 1
y = 2
x + y

"""add_numbers is a function that takes two numbers and adds them together."""
def add_numbers(x, y):
    return x + y
add_numbers(1, 2)

def add_numbers(x, y):
    return x + y
add_numbers(1, 2)


"""add_numbers updated to take an optional 3rd parameter. Using print allows 
printing of multiple expressions within a single cell."""
def add_numbers(x,y,z=None):
    if (z==None):
        return x+y
    else:
        return x+y+z
print(add_numbers(1, 2))
print(add_numbers(1, 2, 3))

"""add_numbers updated to take an optional flag parameter."""
def add_numbers(x, y, z=None, flag=False):
    if (flag):
        print('Flag is true!')
    if (z==None):
        return x + y
    else:
        return x + y + z
print(add_numbers(1, 2, flag=True))

"""Assign function add_numbers to variable a."""
def add_numbers(x,y):
    return x+y
a = add_numbers
a(1,2)

"""Use type to return the object's type."""
type('This is a string')
type(None)
type(1)
type(1.0)
type(add_numbers)

"""Tuples are an immutable data structure (cannot be altered)."""
x = (1, 'a', 2, 'b')
type(x)

"""Lists are a mutable data structure."""
x = [1, 'a', 2, 'b']
type(x)

"""Use append to append an object to a list."""
x.append(3.3)
print(x)

"""This is an example of how to loop through each item in the list."""
for item in x:
    print(item)

"""Or using the indexing operator:"""
i=0
while( i != len(x) ):
    print(x[i])
    i = i + 1

"""Use + to concatenate lists."""
[1,2] + [3,4]

"""Use * to repeat lists."""

[1]*3

"""Use the in operator to check if something is inside a list."""
1 in [1, 2, 3]

"""Now let's look at strings. Use bracket notation to slice a string."""
In [ ]:

x = 'This is a string'
print(x[0]) #first character
print(x[0:1]) #first character, but we have explicitly set the end character
print(x[0:2]) #first two characters
​

This will return the last element of the string.
In [ ]:

x[-1]

This will return the slice starting from the 4th element from the end and stopping before the 2nd element from the end.
In [ ]:

x[-4:-2]

This is a slice from the beginning of the string and stopping before the 3rd element.
In [ ]:

x[:3]

And this is a slice starting from the 3rd element of the string and going all the way to the end.
In [ ]:

x[3:]
In [ ]:

firstname = 'Christopher'
lastname = 'Brooks'
​
print(firstname + ' ' + lastname)
print(firstname*3)
print('Chris' in firstname)
​

split returns a list of all the words in a string, or a list split on a specific character.
In [ ]:

firstname = 'Christopher Arthur Hansen Brooks'.split(' ')[0] # [0] selects the first element of the list
lastname = 'Christopher Arthur Hansen Brooks'.split(' ')[-1] # [-1] selects the last element of the list
print(firstname)
print(lastname)

Make sure you convert objects to strings before concatenating.
In [ ]:

'Chris' + 2
In [ ]:

'Chris' + str(2)

Dictionaries associate keys with values.
In [ ]:

x = {'Christopher Brooks': 'brooksch@umich.edu', 'Bill Gates': 'billg@microsoft.com'}
x['Christopher Brooks'] # Retrieve a value by using the indexing operator
​
In [ ]:

x['Kevyn Collins-Thompson'] = None
x['Kevyn Collins-Thompson']

Iterate over all of the keys:
In [ ]:

for name in x:
    print(x[name])

Iterate over all of the values:
In [ ]:

for email in x.values():
    print(email)

Iterate over all of the items in the list:
In [ ]:

for name, email in x.items():
    print(name)
    print(email)

You can unpack a sequence into different variables:
In [ ]:

x = ('Christopher', 'Brooks', 'brooksch@umich.edu')
fname, lname, email = x
In [ ]:

fname
In [ ]:

lname

Make sure the number of values you are unpacking matches the number of variables being assigned.
In [ ]:

x = ('Christopher', 'Brooks', 'brooksch@umich.edu', 'Ann Arbor')
fname, lname, email = x


























