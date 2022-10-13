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
        if self.head == None:
            print("Lo sentimos, no hay elementos en la lista")
        else:
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
                anterior = actual.next 

    def imprimir_lista(self):
        if self.head == None:
            print("Lo sentimos, no hay elementos en la lista")
        else:
            actual = self.head
            while actual != None:
                print(str(actual.data), end = ", ")
                actual = actual.next

def actualizar():
    





s = lista()

s.insertar_elemento(1)
s.insertar_elemento(2)
s.insertar_elemento(3)

s.imprimir_lista()


    









