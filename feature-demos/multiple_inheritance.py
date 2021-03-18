class Grandparent:
    def __init__(self):
        print("grandparent init")
        super().__init__()


class ParentA(Grandparent):

    def __init__(self):
        print("parent a init")
        # super().__init__()


class ParentB(Grandparent):

    def __init__(self):
        print("parent b init")
        # super().__init__()


class Child(ParentA, ParentB):

    def __init__(self):
        print("child init")
        super().__init__()


child = Child()

print(Child.__mro__)

print(ParentA.__mro__)
