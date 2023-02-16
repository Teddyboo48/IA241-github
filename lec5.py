#all values and data cantainers are objects
#a=1
#b=2
#id() function returns the identity of an object
#print(id(a))
#print(id(b))
#print(id(1))
#== operator compares the value of 2 objects
#print(a == b)
#is operator compares the identity of 2 objects
#print(a is  b)

#none indicates no value
#a=None
#print(id(a))
#print(id(None))

#print(a is None)
#print(a == None)
#only None can be None 
#x = []
#print(x is None)

#Boolean is True/False
#and or, and not operators
#x and y : If x is false, then x, else y
#print(True and False)
#x or y: if X is False, then y, else x
#print(True or False)
#not x: If x is false, then true, else false
#print(not True)
#empty data containers, empty strings, int 0, float 0.0, and None are all kinds of false
#print(not None)
#print(()and[])
#print([]and())
#print(-1 or 0)
#print(0 or -1)

#IF is used for conditional executions
#if 2<1 :
#    print('2>1')
#    print('another 2>1')
 #   if 3>1:
#        print('3>1')
#else:
#    print('else statement')
#IF-else allows you to define action if conditional test fails

#print('out of if block')

#if else
if 2<1 :
    print('2<1')
else:
    print('2>1')
       
#elif contigency is else fails
if 2>1:
    print('2>1')
elif 3>1:
    print('3>1')
else:
    print('else')
    
    