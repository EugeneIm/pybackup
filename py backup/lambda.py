#LAMBDA SYNTAX
#THERE ARE EXAMPLE SYNTAXES BELOW

x = lambda a : a + 10
print(x(5))


#lambda is a small anonymous function 
#it can have only one expression but any number of arguments. 
#the expression above is just listing the variable "x" which is valued at 5, just has + 10 and it prints that. 

#--------------------------------------------------------------

x = lambda a, b : a * b
print(x(5, 6))


#this is saying there are 2 values, a and b. 
#instead of addition, it uses * which is multiplication so the printed value is 30. 

#---------------------------------------------------------------

#example of how a lambda is used


def myFunction(n):
    return lambda a : a * n

myDoubler = myFunction(2)

print(myDoubler(11))


#the argument of returning a * n is shown. 
#the function of "myDoubler" is equal to running myFunction multiplied by 2
#by valuing "myDoubler" at 11, print(myDoubler(11)), the value that is multiplied is 11. 
    #so the final printed value is 22. 

#---------------------------------------------------------------

#same function definition to make two different functions but in the same program. 


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))


#it runs "mydoubler" and "mytripler" so it will print out 22 and 33. 

#---------------------------------------------------------------