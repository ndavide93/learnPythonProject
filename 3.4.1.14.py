import math
from tkinter import Y
class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__ax=x
        self.__ay=y
        
    def getx(self):
        return self.__ax
       
    def gety(self):
        return self.__ay

    def distance_from_xy(self, x, y):
       return self.distanzaDaO=(((self.__ax - x))**2+(self.__ay-y)**2)**0.5
       

    def distance_from_point(self, point):
        distanzaDaPoint=math.hypot(getx(point)-getx(self),gety(point)-gety(self))
        return distanzaDaPoint
        #self.distanzaDaPoint=((getx(point)-getx(self))**2+(gety(point)- gety(self))**2)**0.5

point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))