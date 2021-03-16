#sample syntax is going to be put underneath

# a variable created in a function is available in that function.

"""
def myFunction():
    x = 10
    print(x)

myFunction()
"""
#above is a local scope.

#this is a function inside a function.

"""
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()
"""

# the local scope can be accessed from a function within a function

# below is going to be a global scope

"""
x = 300

def myfunc():
  print(x)

myfunc()

print(x)
"""

# this will print the vaue of 300 twice because it is a variable created outside the function.

#The function will print the local x, and then the code will print the global x
#it will print the values of 300 and 200 because x = 300 was created outside the function and x = 200 was created inside the function.

"""
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)
"""