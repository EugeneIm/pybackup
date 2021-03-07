
#"def" tri_recursion(k): just defines that "tri_recursion(k)" will do what is written underneath it


def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")      #the syntax prints out "Recursion Example Results" before the results
tri_recursion(4)      #tri_recursion(n) is basically the "print(n) of tri-recursion()"


#I don't necessarily know why if I put (k - 4) it only prints out one "4" even though the brackets in tri_recursion(4) is the value 4. 
  #which should print out the loop 4 times. 
#k - 1 prints out 1, 3, 6, 10. Intervals growing by 1. 1-3 = 2, 3-6 = 3, 6-10 = 4. 



#^^ Keep looking at this and trying it out, learn how it works 
#Figure out how recursions work and then explain the syntax later. 




#PYTHON ALSO ACCEPTS FUNCTION RECURSION, WHICH MEANS A DEFINED FUNCTION CAN CALL ITSELF.

#RECURSION IS A COMMON MATHEMATICAL AND PROGRAMMING CONCEPT. IT MEANS THAT A FUNCTION CALLS ITSELF. 

#THIS HAS THE BENEFIT OF MEANING THAT YOU CAN LOOP THROUGH DATA TO REACH A RESULT.

#THE DEVELOPER SHOULD BE VERY CAREFUL WITH RECURSION AS IT CAN BE QUITE EASY TO SLIP INTO WRITING A FUNCTION WHICH NEVER TERMINATES, 

#OR ONE THAT USES EXCESS AMOUNTS OF MEMORY OR PROCESSOR POWER. HOWEVER, WHEN WRITTEN CORRECTLY RECURSION CAN BE A VERY EFFICIENT AND MATHEMATICALLY-ELEGANT APPROACH TO PROGRAMMING.

#IN THIS EXAMPLE, TRI_RECURSION() IS A FUNCTION THAT WE HAVE DEFINED TO CALL ITSELF ("RECURSE"). 

#WE USE THE K VARIABLE AS THE DATA, WHICH DECREMENTS (-1) EVERY TIME WE RECURSE. THE RECURSION ENDS WHEN THE CONDITION IS NOT GREATER THAN 0 (I.E. WHEN IT IS 0).

#TO A NEW DEVELOPER IT CAN TAKE SOME TIME TO WORK OUT HOW EXACTLY THIS WORKS, BEST WAY TO FIND OUT IS BY TESTING AND MODIFYING 



#This is the literal definition of what recursions are. 