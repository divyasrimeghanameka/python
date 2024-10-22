class Parent:
	def func1(self):
		print("first fun")
class Child:
	def func2(self):
		print("2nd")
class Child1(Child,Parent):
	def func3(self):
		print("3rd")
obj=Child1()
obj.func1()
obj.func2()
obj.func3()
