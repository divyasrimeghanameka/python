class Parent:
	def func1(self):
		print("this is function 1")
class Child(Parent):
	def func2(self):
		print("this is function 2")
class Child1(Child):
	def func3(self):
		print("this is functoin 3")
obj=Child1()
obj.func1()
obj.func2()
obj.func3()
