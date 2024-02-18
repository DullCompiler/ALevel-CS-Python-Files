class GetSet:
    __x=0
    
    def __init__(self,x):
        self.__x = x
        
    def get_x(self):
        return self.__x
    
    def set_x(self, x):
        self.__x = x
        
y=GetSet(12) 
print(y.get_x())