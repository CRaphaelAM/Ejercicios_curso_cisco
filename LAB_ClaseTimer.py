"""
Este programa se encarga de crear una clase Timer que suma o resta segundos a la hora del sistema

Tu clase se llamará Timer (temporizador en español). Su constructor acepta tres argumentos que representan horas (un valor del rango [0..23]; usaremos tiempo militar), minutos (del rango [0. .59]) y segundos (del rango [0..59]).

Cero es el valor predeterminado para todos los parámetros anteriores. No es necesario realizar ninguna comprobación de validación.

La clase en sí debería proporcionar las siguientes facilidades:

    Los objetos de la clase deben ser "imprimibles", es decir, deben poder convertirse implícitamente en cadenas de la siguiente forma: "hh:mm:ss", con ceros a la izquierda agregados cuando cualquiera de los valores es menor que 10.
    La clase debe estar equipada con métodos sin parámetros llamados next_second() y previous_second(), incrementando el tiempo almacenado dentro de los objetos en +1/-1 segundos respectivamente.

Emplea las siguientes sugerencias:

    Todas las propiedades del objeto deben ser privadas.
    Considera escribir una función separada (¡no un método!) para formatear la cadena con el tiempo.

"""

class Timer:
    def __init__(self,hora:int = 0, minutos:int = 0, segundos:int = 0) -> None:
        self.__hora = hora
        self.__minutos = minutos
        self.__segundos = segundos

    def __str__(self):
        h = f"0{self.hora}" if self.hora < 10 else str(self.hora)
        m = f"0{self.minutos}" if self.minutos < 10 else str(self.minutos)
        s = f"0{self.segundos}" if self.segundos < 10 else str(self.segundos)
        
        return f"{h}:{m}:{s}" 
        

    def next_second(self)-> None:
        """
        Este método se encarga de incrementar la cantidad de segundos del temporizador en 1

        No recibe parámetros

        Devuelve None
        """
        if self.segundos == 59:
            self.segundos = 0
            if self.minutos == 59:
                self.minutos = 0
                if self.hora == 23:
                    self.hora = 0
                else:
                    self.hora += 1
            else: self.minutos += 1
        else: self.segundos +=1


    def prev_second(self) -> None:
        """
        Este método se encarga de decrementar la cantidad de segundos del temporizador en 1

        No recibe parámetros

        Devuelve None
        """
        if self.segundos == 0:
            self.segundos = 59
            if self.minutos == 0:
                self.minutos = 59
                if self.hora == 00:
                    self.hora = 23
                else:
                    self.hora -= 1
            else: self.minutos -= 1
        else: self.segundos -= 1


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)