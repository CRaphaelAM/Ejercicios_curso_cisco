"""
El constructor de la clase acepta un argumento: una cadena. La cadena representa el nombre del día de la semana y los únicos valores aceptables deben provenir del siguiente conjunto:

Lun Mar Mie Jue Vie Sab Dom

Invocar al constructor con un argumento desde fuera de este conjunto debería generar la excepción WeekDayError (defínela tu mismo; no te preocupes, pronto hablaremos sobre la naturaleza objetiva de las excepciones). La clase debe proporcionar las siguientes facilidades:

    Los objetos de la clase deben ser "imprimibles", es decir, deben poder convertirse implícitamente en cadenas de la misma forma que los argumentos del constructor.
    La clase debe estar equipada con métodos de un parámetro llamados add_days(n) y subtract_days(n), siendo n un número entero que actualiza el día de la semana almacenado dentro del objeto mediante el número de días indicado, hacia adelante o hacia atrás.
    Todas las propiedades del objeto deben ser privadas.

Completa la plantilla que te proporcionamos en el editor, ejecuta su código y verifica si tu salida se ve igual que la nuestra. Completa la plantilla que te proporcionamos en el editor, ejecuta su código y verifica si tu salida se ve igual que la nuestra.

"""

class WeekDayError(Exception):
    pass
	
class Weeker:
    
    dias = [
        "Lun", # 0 1 1 + 15 1 - 15 -14 -14 + 7 -7 7
        "Mar", # 1 2  
        "Mie", # 2 3  3  rest = pos - n  rest +=7        
        "Jue", # 3 4     17   4-17  -13  -13 + 7  -6  6
        "Vie", # 4 5x  - 10   5 - 10 = -5 -5+7 = 2 
        "Sab", # 5 6
        "Dom"  # 6 7   + 15 = 22    22 - 7 = 15     15 - 7 = 8   8 - 7 = 1 
    ]

    def __init__(self,day:str)->None:
        if day not in self.dias:
            raise WeekDayError
        self.__dia = day


    def __str__(self)->str:
        return f"El dia de la semana es: {self.__dia}"

    def add_days(self, n:int) -> None:
        pos_d = self.dias.index(self.__dia)
        self.__dia = self.dias[(n + pos_d)%7]
            

    def subtract_days(self, n:int) -> None:
        pos_d = self.dias.index(self.__dia)
        self.__dia = self.dias[(pos_d - n)%7]

        pass


try:
    weekday = Weeker('Lun')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Lunes')
except WeekDayError:
    print("Lo siento, no puedo atender tu solicitud.")
    