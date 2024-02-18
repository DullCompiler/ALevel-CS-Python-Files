class Superclass(object):
    def greeting(self):
        raise NotImplementedError("Please Implement this Method")
    
class Subclass(Superclass):
    def notgreeting(self):
        print("Hello World")
        
s=Subclass()
s.greeting()