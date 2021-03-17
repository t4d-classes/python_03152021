

nums = [1, 2, 3, 4, 5]


# imperative
# for (int x=0; x < len(nums); x++) {
#    double_nums.append(nums[x] * 2)
# }

# more declarative
# double_nums = []
# for num in nums:
#     double_nums.append(num * 2)

# more more declarative
def double(x):
    print("called double: " + str(x))
    return x * 2


def my_map(transform_fn, items):

    for item in items:
        yield transform_fn(item)


# double_nums = my_map(double, nums)
# print(double_nums)

double_nums = my_map(double, nums)

print(next(double_nums))
print(next(double_nums))
print(next(double_nums))
print(next(double_nums))
print(next(double_nums))


# for double_num in double_nums:
#     print("in the loop: " + str(double_num))


# double_nums = list(map(lambda x: x * 2, nums))
# print(double_nums)


# def my_map(transform_fn, items):

#     transformed_items = []

#     for item in items:
#         transformed_items.append(transform_fn(item))

#     return transformed_items
