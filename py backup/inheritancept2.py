#__init__() Function
#When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
#To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()


#-------------------------------

#super() Function
#Python also has a super() function that will make the child class inherit all the methods and properties from its parent:


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()

<<<<<<< HEAD
#because there is the "super()" function, it makes the child class inherite the methods and properties from its parent. 

=======
#because there is the "super()" function, it makes the child class inherite the methods and properties from its parent. 
>>>>>>> a26b2c11379f9effc5f051baea80aed30ea1b297
