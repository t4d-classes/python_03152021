
# person = dict(first_name="Bob", last_name="Smith", age=23)

person = {
    "first_name": "Bob",
    "last_name": "Smith",
    "age": 23
}

# person["email"] = "someemail@someemail.org"
# print(person["first_name"])
# person["first_name"] = "Sally"
# print(person["first_name"])
# del person["first_name"]
# print(person)
# person[(1, 2)] = "test"
# print(person[(1, 2)])

# for key in person.keys():
for key in person:
    print(key)

for val in person.values():
    print(val)

for key, val in person.items():
    print(key, val)

# print(person.get("email"))
# print(person.get("email", "somedefault@somedefault.org"))

# print(person.setdefault("middle_name", "Timmy"))
# print(person)

# # remove the last item added
# r = person.popitem()
# print(r)
# print(person)

# print(person.pop("age"))
# print(person)

print("age" in person)
print(2 in [1, 2, 3, 4, 5])

# empty_dict = dict()

# if empty_dict:
#     print("not empty")
# else:
#     print("empty")

# print(len(empty_dict))
# print(len("some string"))
# print(len([]))
