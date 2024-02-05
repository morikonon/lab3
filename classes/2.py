class Shape:
	def __init__(self):
		pass
	def area(self):
		return 0
class Square(Shape):
	def __init__(self,lenght):
		super().__init__(self)
		self.lenght = lenght
	def area(self):
		return self.lenght ** 2
shape = Shape()
print("Area of shape" , shape.area())
square = Square(5)
print("Area of Square" , square.area())
