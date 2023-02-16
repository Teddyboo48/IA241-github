# 3.1
alien_color = 'Red'

if alien_color == 'Green':
    print('You Got 5 Points')
#3.2
else:
    print('You Got 10 Points')
    
# 3.3
favorite_fruits = ['calamondin','peach','lemon']
if 'calamondin' in favorite_fruits:
    print('You Really like Calamondins!')
if 'peach' in favorite_fruits:
    print('You Really Like Peaches!')
if 'lemon' in favorite_fruits:
    print('You Really Like Lemons!')
    
#3.4
age = 20
if age < 10:
    print('This person is a kid')
elif 10 <= age <20:
    print('This person is a teenager')
else: 
    print('This person is an adult')
    if age >= 65:
        print('This person is an elder')