class Facultad:
    __codigo=0
    __nombre=""
    __direccion=""
    __localidad=""
    __telefono=""
    __carrera=object
    def __init__(self, codigo,nombre,direccion,localidad,telefono, carrera):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__direccion=direccion
        self.__localidad=localidad
        self.__telefono=telefono
        self.__carrera=carrera
    
    def mostrarDatos(self):
        cadena=(f'\nFacultad: {self.__nombre}\n')
        cadena+=str(self.__carrera)
        return cadena
    
    def getCodigo(self):
        return self.__codigo
    
    def getNombre(self):
        return self.__carrera.getNombre()
    
    def __str__(self):
        cadena=(f"Codigo de Carrera: {self.__carrera.getCodigo()}\n")
        cadena+= ('Codigo Facultad: {}\nNombre: {}\nLocalidad: {}'.format(self.__codigo, self.__nombre, self.__localidad))
        return cadena
    
    def __del__(self):
        print('Borrando carreras....')
        del self.__carrera
