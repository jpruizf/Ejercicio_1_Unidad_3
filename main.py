from ManejadorFacultades import ManejadorFacultad
from claseMenu import Menu
from claseFacultad import Facultad

if __name__=="__main__":
    menu=Menu()
    lista=ManejadorFacultad()
    lista.cargarDatos()
    menu.ejecutar(lista)
    #del Facultad
    
