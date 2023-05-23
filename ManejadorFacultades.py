import csv
from claseFacultad import Facultad
from claseCarrera import Carrera

class ManejadorFacultad:
    __listaM=[]
    def __init__(self):
        self.__listaM=[]

    def cargarDatos(self):
        archivo=open("Facultades.csv")
        reader = csv.reader(archivo,delimiter=',')
        for fila in reader:
            if "San Juan" in fila or "SanJuan" in fila:
                codigoF=int(fila[0])
                nombreF=fila[1]
                direccion=fila[2]
                localidad=fila[3]
                telefono=fila[5]
            else:
                codigo=int(fila[1])
                nombre=fila[2]
                fecha_inicio=fila[6]
                duracion=fila[4]
                titulo=fila[3]
                carrera = Carrera(codigo, nombre,fecha_inicio, duracion, titulo)
                facultad = Facultad(codigoF, nombreF, direccion, localidad, telefono, carrera)
                self.__listaM.append(facultad)
        archivo.close()

    def opcion1(self, codigo):
        for fila in self.__listaM:
            if codigo == fila.getCodigo():
                print(f"Datos:\n{fila.mostrarDatos()}")

    def opcion2(self, nombre):
        for fila in self.__listaM:
            if nombre == fila.getNombre():
                print(fila)
