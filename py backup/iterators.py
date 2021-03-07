#THERE ARE EXAMPLE SYNTAXES BELOW
#Iterator = object that contains a number of values 
#It can be iterated upon, so basically, you can look through the values and search. 

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#lists, dictionaries, and set are all viable objects to be iterated. 
#the first "print()" associated with the first value in the iterator. 
    #print(next(myit)) -> "apple"
    #print(next(myit)) -> "banana"
    #print(next(myit)) -> "cherry"