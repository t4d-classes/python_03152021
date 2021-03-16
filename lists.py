from functools import reduce

nums = [1, 2, 3, 4, 5]

# list comprehension
double_nums = [num * 2 for num in nums if num > 2]

print(double_nums)
