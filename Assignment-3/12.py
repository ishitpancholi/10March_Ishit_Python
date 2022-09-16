#program class constructed by radius and two methdos which will compute the are anfd the perimeter of circle

class circle():
    def __init__(self,r):
        self.radius=r
    def area(self):
        return self.radius**2*3.14
    def perimeter(self):
        return self.radius*3.14        
newcircle=circle(8)
print(newcircle.area()) 
print(newcircle.perimeter())       
