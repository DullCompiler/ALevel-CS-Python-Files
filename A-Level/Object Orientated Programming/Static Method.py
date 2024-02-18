class myClass:
    @staticmethod #decorator
    def static_method(x):
        print(x)
        
myClass.static_method(2)
c = myClass()
c.static_method(4)