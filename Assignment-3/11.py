#program a class constucted bya length and width and a methond which will compute th area of a rectangle

from turtle import width


class rectangle():
    def __init__(self,l,w):
        self.length=l
        self.width= w
    def rectangle_area(self):
        return self.length*self.width 
newRectangle=rectangle(14,12)
print(newRectangle.rectangle_area())           
    
        