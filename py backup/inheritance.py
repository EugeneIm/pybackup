#Inheritance

#Parent and Child class. 


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()


#The parent class is "Person" 
#---------------------------------

#Creating a child class. This one will be named "student" 
    #but it will inherit the properties and methods from the parent class "person" 


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass      #when you use the "pass" in the syntax
            #you don't want to add anything else. NOTHING ELSE. 

x = Student("Mike", "Olsen")
x.printname()



#since "student" has inhereted the parent class, using x.printname() will print 
    #Mike Olsen just like how 
        #x = person("john", "doe")
        #x.printname() will print out "john doe"

#when you use the "pass" in the syntax
    #you don't want to add anything else. NOTHING ELSE. 

