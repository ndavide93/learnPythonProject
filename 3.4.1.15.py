import math
class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__ax=x
        self.__ay=y
    def getx(self):
        return self.__ax
    def gety(self):
        return self.__ay
    def distance_from_xy(self, x, y):
       return (((self.__ax - x))**2+(self.__ay-y)**2)**0.5
       
    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(),point.gety())#
class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__angoli = [vertice1,vertice2,vertice3]
        
    def perimeter(self):
        perimetro=0
        perimetro += self.__angoli[0].distance_from_point(self.__angoli[1])
        perimetro += self.__angoli[1].distance_from_point(self.__angoli[2])
        perimetro += self.__angoli[2].distance_from_point(self.__angoli[0])

        return perimetro 

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())