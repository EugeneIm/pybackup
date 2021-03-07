
for x in range(6):
    print(x)


#^^ Since x isn't put to anything, it prints all of them from 0 - 5 
    #because it always starts at 0 and 6 characters goes to 5
    #x will print 0, 1, 2, 3, 4, 5

#------------------------------------------------------------

for x in range(2, 6):
    print(x)


#^^ x is in the range of 2 - 6. Which means the second character to the 6th character
    #x will print to be 2, 3, 4, 5

#------------------------------------------------------------

for x in range(2, 30, 3):
    print(x)


#^^ the range is between 2 and 30. The third letter is the incriment of looping. 
    #instead of going 1 by 1, it goes 3 by 3 i.e., 2, 5, 8, etc. 

#------------------------------------------------------------

#ELSE IN FOR LOOP

for x in range(6):
    print(x)
else: 
    print("finally finished")


#^^ since the first part of the code is to print the range of 0-5 (6 characters)
    # once x does not print a number anymore, it will print the msg "finally finished" 

#------------------------------------------------------------


#BREAK THE LOOP Just like how in JS theres (i = 0; i < 20; 1++). It stops printing the variable after it reaches 19. 
#However in this it just uses if x == 3: break. (Much simpler and more convenient)


for x in range(6):
    if x == 3: break
    print(x)
else: 
    print("done")



#if you look at the code and don't know how it reads top to bottom, you would expect the end to print "done"
    #but when you do a "break" statement. the rest of the code does NOT get executed. 

#------------------------------------------------------------

#NESTED LOOPS

#adj = ["red", "big", "tasty"]
#fruits = ["apple", "banana", "cherry"]


for x in adj:
    for y in fruits:
        print(x, y)


#since "for y" is nested inside the adj loop, when print(x, y) is executed, 
    #each word will be printed with each fruit. red apple, red banana, red cherry, etc. 

#------------------------------------------------------------

