#THERE ARE EXAMPLE SYNTAXES BELOW


x = 1

if x>3 :
    print("true")
else:
    print("false")
        
#else statements like in JavaScript 
#if one statement doesn't happen or does not get triggered, the second one will
#but also you can have multiple if/else statements just like JS


#--------------------------------------

#while loop with a break statement
#since at one point "i" will be equal to 3 after 3 loops, it will BREAK the loop after it reaches the value of 3


i = 0
    #0, 1, 2, 3.
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

#This breaks the loop when it reaches the value of 3. i += 1 is the PY equivalent to i++ in JS

#------------------------------------


i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#while loop with continue statement
#when "i" is equal to 3, skip the print(i) of "3". 
    #0, 1, 2, 4, 5 ,6 

