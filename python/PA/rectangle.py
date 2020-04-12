class rectangle:
	def __init__(self, width, height):
		self._width=width
		self._height=height
	def calculate_area(self):
		return self._width*self._height
	def calculate_perimeter(self):
		return (self._height+self._height)*2
	def __str__(self):
		return 'Width: {0}, Height: {1}, Area: {2}, Perimeter: {3}'.format(self._width, self._height, self.calculate_area(), self.calculate_perimeter())