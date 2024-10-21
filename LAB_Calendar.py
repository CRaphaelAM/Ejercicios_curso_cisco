"""
Este programa calcula las ocurrencias de un día de la semana en un año
"""

import calendar

class MyCalendar(calendar.Calendar):

    def __init__(self):
        super().__init__()

    def count_weekday_in_year(self,/,year:int, weekday:int) -> int:
        
        """
        El método se encarga de contar las ocurrencias de un día de la semana en todo el año especificado

        Devuelve la cantidad de ocurrencias como un valor entero
        """
        counter:int = 0
        for mes in range(1,13):
            dias_mes:list[list[tuple]] = self.monthdays2calendar(year,mes)
            
            for semana in dias_mes:
                for dia in semana:
                    counter+= 1 if dia[1] == weekday and dia[0] != 0 else 0
        return counter

def main():
    cal = MyCalendar()
    error = True
    
    while error:
        try:
            anno = int(input("Ingrese el año: "))
            dia = int(input("Ingrese el día de la semana que desea contar. Debe ser un valor entre 0 y 6: "))
            if anno > 9999 or anno < 1000:
                raise Exception()
            if dia < 0 or dia > 6:
                raise Exception()
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print("El año o día ingresado no es válido")
        else: error = False

    print(f"La cantidad de veces que se repite el {dia} es: {cal.count_weekday_in_year(year = anno,weekday = dia)}")

if __name__ == "__main__":
    main()