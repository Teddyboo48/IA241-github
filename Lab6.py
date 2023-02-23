'''
Hayden Knight
Lab 6
'''

#3.1
for i in range(6):
    if i !=3:
        print(i)

#3.2
result = 1
for i in range(1, 6):
    result = result * i
    
print(result)

#3.3
sum = 0
for i in range (1,6):
    sum += i
    
print(sum)

#3.4
product= 1
for i in range(3,9):
    product *= i
    
print(product)

#3.5
numerator = 1
for n in range(8,0,-1):
    numerator *= n
#print(numerator)

denominator = 1
for d in range(3,0,-1):
    denominator *= d
#print(denominator)
    
answer= numerator/denominator
print(answer)
#3.6

result= 0

for word in 'this is my 6th string' .split():
    result=result +1
    
print(result)

#3.7
my_tweet= { 
"favorite_count":1138, 
"lang": "en", 
"coordinates": (-75, 40), 
"entities":{"hashtags":["Preds","Pens","SingIntoSpring"]}}

hashtags_count=0
for hashtags in my_tweet['entities']['hashtags']:
    hashtags_count += 1
print(hashtags_count)