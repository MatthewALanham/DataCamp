import pandas as pd
x = 1
print (x)
x = [1,2,"3",4]
x[1]
#zero indexing
x[0]
#negative indexing; here -1 is same as 3
x[-1]
x[3]
#list slicing; first included; last excluded
x[0:2]
#getting all elements after index
x[1:]
#getting all elements prior to end index
x[:3]
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area = areas[3]+areas[7]

# Print the variable eat_sleep_area
print(eat_sleep_area)

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs (first 6 elements)
downstairs = areas[0:6]

# Use slicing to create upstairs (last four elements)
upstairs = areas[6:11]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Alternative slicing to create downstairs (first 6 elements)
downstairs = areas[:6]

# Alternative slicing to create upstairs (last four elements)
upstairs = areas[6:]

x = [["a", "b", "c"],
     ["d", "e", "f"],
     ["g", "h", "i"]]
print(x)
x[2][0]
x[2][:2]

###################################
# List manipulation
###################################
# when you copy a list using "=" you are copying the reference to the list
# thus if y=x, when you change an element in y it will change it in x too.

# Uf you don't want that to happen and want to do a copy without references,
# then do this y=list(x) OR y=x[:]

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area to 10.50
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4] = "chill zone"

# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1 ["poolhouse", 24.5]
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2 "garage" and float 15.45
areas_2 = areas_1 + ["garage", 15.45]
print(areas_2)

# delete ["poolhouse", 24.5]
print(areas_2[-4:-2])
del(areas_2[-4:-2])

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy that reference the same data
areas_copy = areas
# creates a copy that does not reference the same data
#areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
type(areas)
type(areas[1])
###################################
# Functions
###################################
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)

help(type)
help(max)
#works in iPython ?max
help(sorted)

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second
#print(full)
# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)

# Print out full_sorted
print(full_sorted)
###################################
# Methods
###################################
# methods are functions that belong to python objects
# everything in python is an object and objects have specified methods
# associated to them by object type

# string to experiment with: place
place = "poolhouse"

# Use upper() on place: place_up
place_up = place.upper()

# Print out place and place_up
print(place); print(place_up)

# Print out the number of o's in place
print(place.count('o'))

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse (24.5) and garage size (15.45)
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)
###################################
# Packages
###################################
# Packages are a directory of python scripts
# Each python script is a module
# https://pip.pypa.io/en/stable/installation/
# from terminal: python3 get-pip.py
# conda install -c conda-forge numpy
# https://repo.anaconda.com/archive/.winzip/
# In Spyder - go to Tools-> PYTHONPATH Manager and add path to where
# libraries are located/installed

# Import the math package
import math
#import numpy as np

# Definition of radius
r = 0.43

# Calculate C
C = 2*math.pi*r

# Calculate A
A = math.pi*(r**2)

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))

# Import radians function of math package
from math import radians

# Definition of radius
r = 192500

# Travel distance of Moon over 12 degrees. Store in dist.
dist = r * radians(12)

# Print out dist
print(dist)

###################################
# NumPy
###################################
# python doesn't know how to do calculations on lists
# NumPy stands for 'Numeric Python' and provides an alternative
# to python lists, specifically a NumpPy Array so you can do calcs
# Numpy arrays contain only one data type
import numpy as np
areas_num = np.array(areas)

# Import the numpy package as np
import numpy as np

# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))

# Import numpy
import numpy as np

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m = np_height_in * 0.0254

# Print np_height_m
print(np_height_m)

# Import numpy
import numpy as np

# Create array from height_in with metric units: np_height_m
height_in = [1.73, 1.68, 1.71, 1.89, 1.79]
np_height_m = np.array(height_in) * 0.0254

# Create array from weight_lb with metric units: np_weight_kg
weight_lb = [65.4, 59.2, 63.6, 88.4, 68.7] 
np_weight_kg = np.array(weight_lb) * 0.453592

# Calculate the BMI: bmi
bmi = np_weight_kg / (np_height_m ** 2)

# Print out bmi
print(bmi)

# Import numpy
import numpy as np

# Calculate the BMI: bmi
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array
light = bmi < 21

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])


