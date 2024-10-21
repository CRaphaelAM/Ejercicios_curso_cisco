"""
    Se llama Point.
    Su constructor acepta dos argumentos (x y y respectivamente), ambos por defecto se igualan a cero.
    Todas las propiedades deben ser privadas.
    La clase contiene dos métodos sin parámetros llamados getx() y gety(), que devuelven cada una de las dos coordenadas (las coordenadas se almacenan de forma privada, por lo que no se puede acceder a ellas directamente desde el objeto).
    La clase proporciona un método llamado distance_from_xy(x,y), que calcula y devuelve la distancia entre el punto almacenado dentro del objeto y el otro punto dado en un par de números flotantes.
    La clase proporciona un método llamado distance_from_point(point), que calcula la distancia (como el método anterior), pero la ubicación del otro punto se da como otro objeto de clase Point.

"""




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


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))