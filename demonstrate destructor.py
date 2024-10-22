class Cons:
	def __init__(self):
		self.greet="good morning"
	def display(self):
		print("msg=",self.greet)
	def __del__(self):
		print("object is destroyes")
obj=Cons()
obj.display()
print(obj)
del obj
