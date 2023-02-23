#for loop
#iterates over the items of any sequence (a list or string), in the order that they appear in the sequence
#for item in sequence

for num in [1,2,3]:
    if num>1:
        print(num)
    
for word in 'this is lecture 6'.split():
    print(word)
    for c in word:
        print(c)

#Range Generates arithmetic progressions
#range (M): generates from 0 to m-1
#range (n,m): gnerates progression from n to m-1
#range (n,m,step): generates progression from n to m-1 with an increment of the step

for i in range(5):
    print(i)
    
for i in range(1,5):
    print(i)
    
for i in range(1,5,2):
    print(i)
    
#Breakpoint to debug each code

#Algorithm is a mechanical process for solving a category of problems
#Designing algorithms is interesting, intellectually challenging, and a central part of computer science

num_list = [213,321,123,312]

max_item = num_list[0]

for num in num_list:
    if max_item<= num:
        max_item=num
        
print(max_item)

