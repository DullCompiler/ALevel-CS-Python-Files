class Dog:
    def __init__(self, name, breed, age):
        self.age=age
        self.name=name
        self.breed=breed

    def bark(self):
        print("Woof")

    def trick(self):
        return "Sit"

    def setage(self, age):
        self.age=age

d = Dog("princess", "pitbull", 1)
d.bark()
print(d.trick())
newage=input("How old is your dog?: ")
d.setage(newage)
print(d.name, d.breed, d.age)