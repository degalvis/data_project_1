import os, msvcrt, sys, time

class nodo:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class lista: 
    def __init__(self):
        self.head = None

    def lista_vacia(self):
        return self.head == None

    def insertar_elemento(self, dato):
        if self.head == None:
            self.head = nodo(data = dato)
            return
        actual = self.head
        while actual.next:
            actual = actual.next
        actual.next = nodo(data = dato)

    def eliminar_nodo(self, elemento):
        if self.head != None:
            anterior = None
            actual = self.head
            while actual != None and actual.dato != elemento:
                anterior = actual
                actual = actual.next
            if actual == None:
                print("El elemento no se encuentra en la lista")
            elif anterior == None:
                actual = actual.next
            else:
                anterior.next = actual.next
        else:
            print("Lista vacía, debes ingresar datos primero")
            return
                
    def imprimir_lista(self):
        if self.head == None:
            print("Lo sentimos, no hay elementos en la lista")
        else:
            actual = self.head
            while actual != None:
                print(actual.data, end = " -> ")
                actual = actual.next

def actualizar():
    

        f.write("Actualización \n")
        while actual != None:
            f.write(actual.data)
            f.write("\n")
            actual = actual.next
        f.close()

def MostrarMenu():
  print(   " ----------------------------------------------------------------- "   ) 
  print(   "1.  Insertar elemento"   ) 
  print(   "2.  Imprimir datos"   ) 
  print(   "3.  Borrar elemento"   )
  print(   "4.  Actualizar archivo"   )
  print(   "5.  Salir"   ) 
  print(   " -----------------------------------------------------------------"   ) 

def cls(): #Clean console
    os.system('cls' if os.name=='nt' else 'clear')

def wait(): #Wait until user press a key
    print("Presiona una tecla para continuar")
    msvcrt.getch()

class main():
    s = lista()
    choice = 0

    while True:
        MostrarMenu()
        
        try:
            choice = int(input("Ingrese una opción "))
        except ValueError:
            print("Debes ingresar uno de los valores en el menú")
            print("Intentalo de nuevo")
            wait()
            cls()

        if choice < 1 or choice > 5:
            print("Fuera de rango, intentalo de nuevo")
            time.sleep(3)
            cls()
            continue
        elif choice == 1:
            dato = input("Ingrese el número ")
            s.insertar_elemento(dato)
            cls()
            print("El elemento fue añadido a la lista")
            wait()
            cls()

        elif choice == 2:
            print("Estos son los datos actuales:")
            s.imprimir_lista()
            wait()
            cls()

        elif choice == 3:
            print("Los elementos de la lista son: ")
            s.imprimir_lista()
            aEliminar = input("Ingresa el elemento a eliminar tal y como se encuentra en la lista ")            
            s.eliminar_nodo(aEliminar)
            cls()

            print("Ahora los elementos de la lista son: ")
            s.imprimir_lista()
            wait()
            cls()
        
        elif choice == 4:
            print("Con este método actualizaras el archivo de texto ")
            print("y se te mostrarán los elementos que estén actualmente ")
            print("en la lista")
            wait()
            cls()
            print("Los elementos son: ")
            s.imprimir_lista()
            s.actualizar()
            print("El archivo ha sido actualizado. abrelo para ver los datos")
            wait()
            cls()

        elif choice == 5:
            sys.exit()
