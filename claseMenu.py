class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = {
            1:self.opcion1,
            2:self.opcion2,
            3:self.opcion3
        }

    def opcion1(self, manejadorF):
        print("Mostrar datos una Facultad y sus Carreras.")
        codigo=int(input("Ingresar Codigo de una Facultad: "))
        manejadorF.opcion1(codigo)
   
    def opcion2(self, manejadorF):
        print("Mostrar datos de una Facultad.")
        nombre=input("Ingresar nombre de una carrera: ")
        manejadorF.opcion2(nombre)

    def opcion3(self):
        print("Usted esta saliendo del Programa")
        
        
    def ejecutar(self, manejador):
            while True:
                print("Bienvenido al menú de opciones")
                print("1. Mostrar datos una Facultad y sus Carreras.")
                print("2. Mostrar datos de una Facultad.")
                print("3. Salir")
                op = int(input("Ingrese una Opcion: "))

                # Utilizamos el switcher para llamar a la función correspondiente a la opción seleccionada
                func = self.__switcher.get(op, lambda: print("Opción no válida"))
                if op==1 or op==2:
                    func(manejador)
                else: 
                    func()
                if 3==op:
                    break
