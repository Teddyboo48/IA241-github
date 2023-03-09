'''
Hayden Knight
Lab 8
IA 241
'''

#3.1
def word_count(s):
    words = s.split() 
    return len(words)

#3.2
demo_string = 'Hello World!'
print(word_count(demo_string))

#3.3
def find_min(numbers):
    nums= []
    for num in numbers:
        if type (num) in [int, float]:
            nums.append(num)
    if len(nums) ==0:
        raise ValueError("Input list must contain at least one number")
    min_num = nums[0]
    for num in nums:
        if num < min_num:
            min_num=num
        return min_num

#3.4
demo_list = [1,2,3,4,5,6]
print(find_min(demo_list))

#3.5
mix_list = [1,2,3,4,'a',5,6]
print(find_min(mix_list))