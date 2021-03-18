
# list_a = [1, 2]
# list_b = [1, 2]

# print(id(list_a))
# print(id(list_b))

# tuple_a = (1, 2)
# tuple_b = (1, 3)

# print(id(tuple_a))
# print(id(tuple_b))

# str_a = "hi"
# str_b = "hi"

# print(id(str_a))
# print(id(str_b))


def func_a():
    str_a = "hi"
    print(id(str_a))


def func_b():
    str_b = "hi"
    print(id(str_b))


func_a()
func_b()
