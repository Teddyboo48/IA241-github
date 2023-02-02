#3.1
str_list = ['a','d','e','b','c']
print(str_list.sort())

#3.2
str_list.append('f')
print(str_list)

#3.3
str_list.remove('d')
print(str_list)

#3.4
str_list[2]
print(str_list[2])

#3.5
my_list = ['a','123',123,'d','B','False',False,123,None,'None']
print(len(my_list))

#3.6
my_words = 'This is my third python lab.'
print(len(my_words.split()))
#10 unique items

#3.7
num_list = [12,32,43,35]
num_list.sort()
print(num_list[0])
print(num_list[-1])

#3.8
game_board = [
[0,0,0],
[0,0,0],
[0,0,0]]
print(game_board)

game_board[1][1] = 1
print(game_board)