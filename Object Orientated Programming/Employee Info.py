class Employee(): 
	#constructor 
	def __init__(self,name,dob,salary): 
		self.name=name
		self.dob=dob 
		self.salary=salary
	def details(self):
		print(self.name)
		print(self.dob)
		print(self.salary)
        
# Object Instantiation 
Fred=Employee("Fred","26th April 2000","£40,000") 
Lucy=Employee("Lucy","5th May 2003","£23,000")

Fred.details()
Lucy.details()