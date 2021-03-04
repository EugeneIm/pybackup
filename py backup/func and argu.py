#NTOES FOR FUNCTIONS

"""
def myFunction():
    print("how about no")

myFunction()
"""
    #def myFunction():
        #print("how about no")
                #^ this is defining WHAT the function will do when called. 

"""
myFunction()
"""

    #^this is used to call the function and everything inside the function will
        #be run once called. 

#------------------------------------------------------------

#ARGUMENTS
"""
def my_Functiom(fname):
    print(fname + " refsnes")

my_Functiom("email")
my_Functiom("tobias")
my_Functiom("linus")
"""

#since my_Function() has been defined to print the name in the brackets _ + " refsnes"
    #it will print all that is in the function brackets and then + " refsnes"

#------------------------------------------------------------

#Number of Arguments Possible

"""
def my_Function(fname, lname):
    print(fname + " " + lname)

my_Function("email")
"""

#^^ the function above expects 2 arguments but only gets 1. 

#------------------------------------------------------------

#Arbitrary Arguments // *args

"""
def myFunction(*kids):
    print("the youngest kid is " + kids[2])

myFunction("emil", "tobias", "linus")
"""

#the reason it only prints linus is because the [2] is the 2nd character 
    #i.e., if you did kids[0], it would print "the youngest kid is emil", etc. 

#------------------------------------------------------------

