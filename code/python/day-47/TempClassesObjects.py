class Circle(object):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
    def addrad(self,r):
        self.radius=self.radius+r
    

C1 = Circle(10, 'Red')
print(C1.radius)
print(C1.color)
C1.addrad(15)
print(C1.radius)

#class Rectangle(object):
