

# def do_it(p1, p2=5, p3=10):
#     print(p1, p2, p3)


# do_it(2, 3, p3=1)

# def do_it(p1, p2, *args, **kwargs):
#     print(p1, p2, args, kwargs)


# do_it(1, 2, 3, 4, 5, 6, 7, 8, 9, 0, name="Bob", age=23, size="tall")

# class Person:
#     # def __init__(self, first_name, last_name):
#     #     self.first_name = first_name
#     #     self.last_name = last_name

#     def __init__(self, **kwargs):
#         self.__dict__.update(kwargs)


# person = Person(first_name="Bob", age=23)

# print(person.first_name)

# # variable = result of an expression
# nums = [1, 2, 3, 4, 5]

# # variable: a = expression: 1
# # * is on the variable side of assignment - packing/capturing
# def do_it(a, b, *other):  # * packing/capturing
#     print(a, b, other)

# # * is on the expression side of assignment - unpacking/spreading
# # * unpacking/spreading
# do_it(*nums)

nums = [1, 2, 3, 4, 5]

(a, b, *left_over) = nums
print(a, b, left_over)

other_nums = [*nums, 3, *left_over]
print(other_nums)
