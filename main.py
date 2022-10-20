import os
import msvcrt

class nodo:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class lista: 
    def __init__(self):
        self.head = None

    def crear_lista(self):
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
            while actual != None and actual.data != elemento:
                anterior = actual
                actual = actual.next
            if actual == None:
                print("El elemento no se encuentra en la lista")
            elif anterior == None:
                actual = actual.next
            else:
                anterior.next = actual.next
                
    def imprimir_lista(self):
        if self.head != None:
            actual = self.head
            while actual != None:
                print(actual.data, end = ", ")
                actual = actual.next

    def actualizar(self):
        f = open("archico.txt", "w")
        actual = self.head

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

    while True:
        MostrarMenu()
        choice = int(input("Ingrese una opción "))
        s = lista()

        if choice == 1:
            dato = int(input("Ingrese el número")) #Lack of exception handling
            s.insertar_elemento(dato)
            cls()
            print("El elemento fue añadido a la lista")
            wait()
            cls()

        elif choice == 2:
            print("Estos son los datos actuales.")
            s.imprimir_lista()
            wait()
            cls()

        elif choice == 3:
            print("Los elementos de la lista son: ")
            s.imprimir_lista()
            aEliminar = input("Ingresa el elemento a eliminar tal y como se encuentra en la lista ")

            s.eliminar_nodo(aEliminar)
            print("Ahora los elementos de la lista son: ")
        
        elif choice == 4:
            print("""
                Con este método actualizaras el archivo de texto y se te mostran 
                los elementos que estén actualmente en la lista
                Los elementos son: """)

            s.imprimir_lista()






        elif choice == 4:
            s.actualizar()


        





s = lista()

s.insertar_elemento(3)
s.insertar_elemento("3")
s.insertar_elemento("3")
s.insertar_elemento("3")
s.insertar_elemento("Jose")

s.actualizar()

s.eliminar_nodo("Jose")
s.insertar_elemento("Manuela")

s.imprimir_lista()

s.actualizar()


    









