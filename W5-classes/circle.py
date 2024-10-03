
class Circle:
    pi = 3.1415926535

    def __init__(self):
        self.radius = 0
        self.color = "transparent"

    def getColor(self):
        return self.color
    
    def getCircum(self):
        return 2 * self.pi * self.radius
    
a = Circle()
a.radius = 3
#print(a.getColor) 
print(a.getColor())
print(a.getCircum())
