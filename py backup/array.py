#PY ARRAYS

#Arrays are used to store multiple values. 
#An array is a special variable which holes more than one value at a time. 


cars = ["ford", "honda", "benz"]
x = cars[1]

print(x)

#this will print "honda"

#-------------------------

#ArrayLen


cars = ["ford", "honda", "benz"]
x = len(cars)

print(x)

#this will print '3' because the length of the array is 3 words, etc. 

#-------------------------

#Arrays can also have for loops


cars = ["Ford", "Volvo", "BMW"]

for x in cars:
  print(x)


#-------------------------

#appending arrays and removing elements from an array


cars = ["Ford", "Volvo", "BMW"]

cars.append("Honda") 
print(cars)


#this adds "honda" to the end of the array so printing cars will be "ford" "volvo" "bmw" "honda"


cars = ["Ford", "Volvo", "BMW"]

cars.pop(1)

print(cars)

#this removes the second item in the array. 
    #Therefore, when you print cars, it will only show "ford" and "BMW"
#"pop" just deletes a part from the array. 

#-------------------------


#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the first item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list
