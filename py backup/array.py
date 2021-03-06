#PY ARRAYS

#Arrays are used to store multiple values. 
#An array is a special variable which holes more than one value at a time. 

"""
cars = ["ford", "honda", "benz"]
x = cars[1]

print(x)
"""
#this will print "honda"

#-------------------------

#ArrayLen

"""
cars = ["ford", "honda", "benz"]
x = len(cars)

print(x)
"""

#this will print '3'

#-------------------------

#Arrays can also have for loops

"""
cars = ["Ford", "Volvo", "BMW"]

for x in cars:
  print(x)
"""

#-------------------------

#appending arrays and removing elements from an array

"""
cars = ["Ford", "Volvo", "BMW"]

cars.append("Honda") 
print(cars)
"""

#this adds "honda" to the end of the array so printing cars will be "ford" "volvo" "bmw" "honda"

"""
cars = ["Ford", "Volvo", "BMW"]

cars.pop(1)

print(cars)
"""
#this removes the second item in the array. 
    #Therefore, when you print cars, it will only show "ford" and "BMW"

#-------------------------

