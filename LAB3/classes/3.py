from two import Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    
    def area(self):
        self.areaShape = self.length * self.width
        print(self.areaShape)