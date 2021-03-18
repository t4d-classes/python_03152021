from functools import reduce

nums = [1, 2, 3, 4, 5]

# nums_gt3 = list(filter(lambda x: x > 3, nums))

# print(nums_gt3)

# print(sum(nums))


def my_sum(acc, cur):
    print("acc:", acc, "cur:", cur)
    return acc + cur


sum = reduce(my_sum, nums, 0)

print(sum)
