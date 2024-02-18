class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"
    
class Bird(Animal):
    def make_sound(self):
        return "Tweet!"

class Pet:
    def __init__(self, name, animal, age):
        self.name = name
        self.animal = animal
        self.age = age
    
    def make_sound(self):
        return self.animal.make_sound()

class Zoo:
    def __init__(self):
        self.animals = []
    
    def make_sounds(self):
        for animal in self.animals:
            print(animal.make_sound())
            
    def get_oldest_animal(self):
        oldest=0
        for animal in self.animals:
            if int(animal.age)>oldest:
                oldest = int(animal.age)
        print("The oldest animal is", oldest)
   
    def add_animal(self, animal):
        self.animals.append(animal)

# Example usage
dog = Dog("Fido", 3)
cat = Cat("Whiskers", 5)
bird = Bird("Tweety", 2)
pet_dog = Pet("Buddy", dog, 3)
pet_cat = Pet("Mittens", cat, 5)
pet_bird = Pet("Chirpy", bird, 2)
zoo = Zoo()
zoo.add_animal(pet_dog)
zoo.add_animal(pet_cat)
zoo.add_animal(pet_bird)
zoo.get_oldest_animal()
zoo.make_sounds()