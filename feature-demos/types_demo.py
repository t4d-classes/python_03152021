

t = "hello"
print(type(t))

t = 2
print(type(t))

t = 3.4
print(type(t))

t = True
print(type(t))

t = ("a",2,True)
print(type(t)) # tuple is immutable, collection of related items

t = [1,2,3,4,5]
print(type(t)) # list is mutable, collection of multiple kinds of an item

def my_func():
    pass

print(type(my_func))

t = my_func
print(type(t))

t = None
print(type(t))

t = str(5)
print(type(t))

t = int("5")
print(type(t))
print(t)

t = float(4)
print(type(t))
print(t)




