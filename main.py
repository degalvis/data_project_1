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
        self.head = node(data = dato)
        return
    actual = self.head
    while actual.next:
        actual = actual.next
    actual.next = node(data=dato)

def eliminar_nodo(self, elemento):
    def delete_node(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None