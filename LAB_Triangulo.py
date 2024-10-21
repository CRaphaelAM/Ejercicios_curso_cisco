from __future__ import annotations 
import math


class Point:
    def __init__(self, x:float=0.0, y:float=0.0)->None:
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x:float, y:float) -> float:
        return math.hypot((self.__x - x),(self.__y - y))
    

    def distance_from_point(self, point)->float:
        return math.hypot((self.__x - point.getx()),(self.__y - point.gety()))


class Triangle:
    def __init__(self, vertice1:Point, vertice2:Point, vertice3:Point):
        self.p1 = vertice1
        self.p2 = vertice2
        self.p3 = vertice3

    def perimeter(self):
        return self.p1.distance_from_point(self.p2) + self.p1.distance_from_point(self.p3) + self.p2.distance_from_point(self.p3)


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
    