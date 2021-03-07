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

#---------------------------------------------------

mystr = "watermelon"  #prints out "a, p, p, l, e, s" in a list 
myit = iter(mystr)
        #it doesn't matter if there are more characters than the   
        #amount of "print(next(myit))" it will only print the exact amount. 
            #"watermelon" printed out "w, a, t, e, r ,m" and not the whole thing. 
            #each print(next(myit)) represents one character if there is one value and one value if there are multiple. 
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#if there is only 1 value but multiple "print(next(myit))" it prints the characters one by one 

#-------------------------------------------------

#Loopint through an interator. For loops are used here. 

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

#Just like how in a for loop for JS, it prints it continually until there is no more that can be printed. 