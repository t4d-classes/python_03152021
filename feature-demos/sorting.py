from random import randint


def rand_name():
    return "".join([chr(randint(65, 90)) for _ in range(4)])


# names = [rand_name() for _ in range(100)]

# # names.sort()
# sorted_names = sorted(names)

# print(names)
# print(sorted_names)


class Person:
    def __init__(self, person_id, name, age):
        self.id = person_id
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.id} {self.name} {self.age}"


persons = [Person(randint(1, 10000), rand_name(), randint(1, 10))
           for num in range(1000)]

# print(sorted(persons, key=lambda p: p.id))
# print(sorted(persons, key=lambda p: p.name))
# persons.sort(key=lambda p: p.name)

# print(sorted(persons, key=lambda p: f"{str(p.age).ljust(5)}|{p.name}"))
sorted_persons = sorted(
    persons,
    key=lambda p: f"{str(p.age).rjust(5)}|{p.name}")

for person in sorted_persons[100:120]:
    print(person)
