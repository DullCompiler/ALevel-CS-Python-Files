class Animal:
    def __init__(self, name):
        self.name = name
        self._age = 0 # private attribute

    def make_sound(self):
        pass

    def get_age(self):
        return self._age

    def set_age(self, age, vali):
        while vali==False:
            age=input("Please enter the animal's age: ")
            
            
        self._age = age

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Person:
    def __init__(self, name, pet):
        self.name = name
        self.pet = pet

    def greet(self):
        return f"Hi, I'm {self.name} and my pet {self.pet.name} says {self.pet.make_sound()}!"

    @staticmethod
    def say_hello():
        return "Hello!"

# Example usage:

dog = Dog("Fido")
cat = Cat("Whiskers")

person = Person("Alice", dog)
print(person.greet()) # prints "Hi, I'm Alice and my pet Fido says Woof!"

person.pet = cat # type: ignore
print(person.greet()) # prints "Hi, I'm Alice and my pet Whiskers says Meow!"

# Using static method
print(Person.say_hello()) # prints "Hello!"