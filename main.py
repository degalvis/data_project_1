class nodo:
    def crear_nodo(self, data = None, next = None):
        self.data = data
        self.next = next

class lista: 
    def crear_lista(self):
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
        actual.next = nodo(data=dato)

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
                anterior = actual.next 

    def imprimir_lista(self):
        if self.head != None:
            actual = self.head
            while actual != None:
                print(actual.data + ", ")
                actual = actual.next


s = lista()

s.insertar_elemento(1)
s.insertar_elemento(2)
s.insertar_elemento(3)

s.imprimir_lista()









