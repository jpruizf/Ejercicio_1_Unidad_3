from claseFacultad import Facultad

class Carrera:
    __codigo=0
    __nombre=""
    __fecha_inicio=""
    __duracion=""
    __titulo=""
    def __init__(self, codigo,nombre,fecha,duracion,titulo):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__fecha_inicio=fecha
        self.__duracion=duracion
        self.__titulo=titulo
    
    def __str__(self):
        cadena=(f'Nombre Carrera: {self.__nombre}\nDuracion: {self.__duracion}')
        return cadena
    
    def getCodigo(self):
        return self.__codigo
    
    def getNombre(self):
        return self.__nombre
