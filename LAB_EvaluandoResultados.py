from __future__ import annotations
import json


"""
El profesor Jekyll dirige clases con estudiantes y regularmente toma notas en un archivo de texto. Cada línea del archivo contiene 3 elementos: el nombre del alumno, el apellido del alumno y el número de puntos que el alumno recibió durante ciertas clases.

Los elementos están separados con espacios en blanco. Cada estudiante puede aparecer más de una vez dentro del archivo del profesor Jekyll.

Tu tarea es escribir un programa que:

    * Pida al usuario el nombre del archivo del profesor Jekyll.
    * Lea el contenido del archivo y cuenta la suma de los puntos recibidos por cada estudiante.
    * Imprima un informe simple (pero ordenado)

    Nota:

    Tu programa debe estar completamente protegido contra todas las fallas posibles: la inexistencia del archivo, el vacío del archivo o cualquier falla en los datos de entrada; encontrar cualquier error de datos debería causar la terminación inmediata del programa, y lo erróneo deberá presentarse al usuario.
    Implementa y usa tu propia jerarquía de excepciones: la presentamos en el editor; la segunda excepción se debe generar cuando se detecta una línea incorrecta y la tercera cuando el archivo fuente existe pero está vacío.

Consejo: Emplea un diccionario para almacenar los datos de los estudiantes.
"""

class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    # Escribe tu código aquí.
    ...


class FileEmpty(StudentsDataException):
    # Escribe tu código aquí.
    ...


class Estudiante:
    def __init__(self,name: str,surname: str,nota: float):
        self.name:str = name
        self.surname:str = surname
        self.nota:float = nota
    
    def to_dict(self) -> dict:
        return {
            "nombre" : self.name,
            "apellido" : self.surname,
            "nota" : self.nota
        }

    @classmethod
    def from_dict(self,d:dict) -> Estudiante:
        return Estudiante(d["nombre"],d["apellido",d["nota"]])

    def __str__(self):
        return (f"Nombre: {self.name: ^10} Apellido: {self.surname: ^10} Nota: {self.nota: ^10}")

def main() -> None:
    file = input("Ingrese el nombre del archivo: ")

    try:
        with open (file,"r") as in_file:
            data_dict: list[dict] = json.load(in_file)
            estudiantes: list[Estudiante] = [Estudiante.from_dict(d) for d in data_dict]

            





    except FileEmpty as FE:
        print(FE)
    except BadLine as BL:
        exit(BL)
    except StudentsDataException as SE:
        exit(SE)
    except Exception as Ex:
        print(f"Ha ocurrido un error inesperado -> {Ex}")
    


if __name__ == "__main__":
    main()