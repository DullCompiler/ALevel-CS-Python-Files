class Cat():
    def talk(self):
        print("Meow")

class Dog():
    def talk(self):
        print("Woof")

class Bird():
    def talk(self):
        print("Chirp")

def makeSound(animal): 
	animal.talk() 

cat = Cat() 
dog = Dog()
bird = Bird()
makeSound(cat) 
makeSound(dog)
makeSound(bird)