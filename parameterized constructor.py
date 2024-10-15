class ad:
	def __init__(self,a,b):
		self.first=a;
		self.second=b;
	def display(self):
		print(self.first)
		print(self.second)
		print(self.first+self.second)
obj=ad(10,20)
obj.display()
