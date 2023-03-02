'''
Lecture 7 IA 241
Hayden Knight
'''

# While loop
#For repeated excution as long as a condition is true
#While condition is true

#i= 5
#while i >0:
#    i= i-1
 #   print(i)
    
#    if i ==3:
#        break
    #i= i-1
    
#Break statement breaks out smallest enclosing for or while loop
#    i=5
#    while i >0:
#        i=i-1
#        print(i)
        
#        if i==3:
#            break

#continue skips the current iteration and goes to the next
#i= 5
#while i >0:
 #   i= i-1
    
 #   if i ==3:
 #       pass
 #   print(i)

#try:
#    print(1/1)
#except :
#    print('handle error2')

#Exceptions are errors during executions
#THe Try clause executes your code
#if no exception occurs, the except clause is skipped
#if an exception occurs, the rest of the try clause is skipped.

'''
Which statement should you use to finish the while loop, break, pass, continue
=Pass
'''

i= 5
while i>0:
    
    
    try:
        print(1/(i-3))
    except:
        continue
    
    i=i-1