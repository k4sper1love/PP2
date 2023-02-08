class Shape:
    def __init__(self):
        self.areaShape = 0
    
    def area(self):
        print(self.areaShape)


class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        self.areaShape = self.length ** 2
        print(self.areaShape)
