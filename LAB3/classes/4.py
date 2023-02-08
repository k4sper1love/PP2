class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print("({},{})".format(self.x,self.y))
    
    def move(self):
        self.x = input("Enter x cord: ")
        self.y = input("Enter y cord: ")

    def dist(self, x2, y2):
        distance = float(((x2 - self.x) ** 2 + (y2 - self.y) ** 2) ** 0.5)
        print(distance)




