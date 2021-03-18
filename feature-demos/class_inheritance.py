# Base/Parent/Superclass
class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Mentor(Person):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

# Child/Subclass


class Student(Person):   # Student is a Person

    def __init__(self, student_id, first_name, last_name, mentor):
        # self.first_name = first_name
        # self.last_name = last_name
        super().__init__(first_name, last_name)
        self.student_id = student_id
        self.mentor = mentor # composition

    # def full_name(self):
    #     return f"{self.first_name} {self.last_name}"

    def record_info(self):
        return f"{self.student_id} {self.last_name}, {self.first_name}"


# person = Person("Bob", "Smith")
# print(person.full_name())

student = Student(1, "Bob", "Smith", Mentor("Sally", "Timmons"))

print(student.full_name())
print(student.record_info())
