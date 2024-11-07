from Paquete import *
class MinHeapBinaryTree:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

    def insert(self, value):
        if self.data == None:
            self.data = value
            return
        if value <= self.data:
            if self.leftchild is None:
                self.leftchild = MinHeapBinaryTree(value)
            else:
                self.leftchild.insert(value)
        else:
            if self.rightchild is None:
                self.rightchild = MinHeapBinaryTree(value)
            else:
                self.rightchild.insert(value)

        self._heapify_up()

    def _heapify_up(self):
        # Realizar "heapify up" para mantener el menor valor en la raíz
        #para verificar si existe el nodo y si es menor que el actual
        if self.leftchild and self.leftchild.data < self.data:
            self.data, self.leftchild.data = self.leftchild.data, self.data
            self.leftchild._heapify_up()
        if self.rightchild and self.rightchild.data < self.data:
            self.data, self.rightchild.data = self.rightchild.data, self.data
            self.rightchild._heapify_up()

    def _heapify_down(self):
        # Realizar "heapify down" para mantener el menor valor en la raíz
        #si el nodo acutal no tiene hijos
        if not self.leftchild and not self.rightchild:
            return
        smallest = self
        #si existe el nodo y su valor es menor que el smallest
        if self.leftchild and self.leftchild.data < smallest.data:
            smallest = self.leftchild
        if self.rightchild and self.rightchild.data < smallest.data:
            smallest = self.rightchild
        #si smallest no es el nodo actual los cambiamos
        if smallest != self:
            self.data, smallest.data = smallest.data, self.data
            smallest._heapify_down()

    def printTree(self, prefix="", is_left=True):
        if not self:
            return
        if self.rightchild:
            self.rightchild.printTree(prefix + ("│    " if is_left else "     "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(self.data))
        if self.leftchild:
            self.leftchild.printTree(prefix + ("     " if is_left else "│    "), True)


    def printTreeIds(self, prefix="", is_left=True):
        if not self:
            return

        if self.rightchild:
            self.rightchild.printTreeIds(prefix + ("│    " if is_left else "     "), False)

        print(prefix + ("└── " if is_left else "┌── ") + f"{self.data.id}")

        if self.leftchild:
            self.leftchild.printTreeIds(prefix + ("     " if is_left else "│    "), True)

    def inOrder(self):
        if not self:
            return

        self.inOrder()
        print(self)
        print("-----------------")
        self.inOrder()

    def postOrder(self):
        if not self:
            return
        self.postOrder()
        self.postOrder()
        print(self)
        print("-----------------")


    """
    def deleteNode(self, value):
        if self.data == None:
            return False
        # Comparar value con el id
        node_value = self.data.id

        if value < node_value:
            if self.leftchild:
                self.leftchild = self.leftchild.deleteNode(value)
        elif value > node_value:
            if self.rightchild:
                self.rightchild = self.rightchild.deleteNode(value)
        else:
            # print("Inicia Eliminación", self.data)
            # Caso 1: Nodo es una hoja (no tiene hijos)
            if self.leftchild is None and self.rightchild is None:
                # print("Ingresa x hoja")
                return None
            # Caso 2: Nodo tiene 2 hijos
            elif self.leftchild is not None and self.rightchild is not None:
                # print("Ingresa x ambos hijos")
                last_node = self._get_last_node()
                # print("Último nodo encontrado:", last_node.data)

                # Reemplazar los datos en el nodo a eliminar con los datos del último nodo
                self.data = last_node.data

                # Restaurar la propiedad de min-heap
                self._heapify_down()
            # Caso 3: Nodo tiene solo un hijo a la izquierda
            elif self.leftchild is not None:
                # print("Ingresa x hijo a la izquierda")
                return self.leftchild
            # Caso 4: Nodo tiene solo un hijo a la derecha
            else:
                # print("Ingresa x hijo a la derecha")
                return self.rightchild

        return self
    """
    def deleteNode(self, value):
        if self.data == None:
            return False
        # Comparar value con el id
        node_value = self.data.id

        if value < node_value:
            if self.leftchild:
                self.leftchild = self.leftchild.deleteNode(value)
        elif value > node_value:
            if self.rightchild:
                self.rightchild = self.rightchild.deleteNode(value)
        else:
            #print("Inicia Eliminación", self.data)
            # Caso 1: Nodo es una hoja (no tiene hijos)
            if self.leftchild is None and self.rightchild is None:
                #print("Ingresa x hoja")
                return None
            # Caso 2: Nodo tiene 2 hijos
            elif self.leftchild is not None and self.rightchild is not None:
                #print("Ingresa x ambos hijos")
                last_node, parent = self._get_last_node()
                #print("Último nodo encontrado:", last_node.data)

                # Reemplazar los datos en el nodo a eliminar con los datos del último nodo
                self.data = last_node.data
                # Eliminar el último nodo
                if parent:
                    if parent.leftchild == last_node:
                        parent.leftchild = None
                    else:
                        parent.rightchild = None
                # Restaurar la propiedad de min-heap
                self._heapify_down()
            # Caso 3: Nodo tiene solo un hijo a la izquierda
            elif self.leftchild is not None:
                #print("Ingresa x hijo a la izquierda")
                return self.leftchild
            # Caso 4: Nodo tiene solo un hijo a la derecha
            else:
                #print("Ingresa x hijo a la derecha")
                return self.rightchild

        return self

    def extractRoot(self):

        if self.data == None:
            return None

        root_value = self.data

        self.deleteNode(root_value.id)

        return root_value

    def _minsuccesor(self, rootNode):
        #print("minsuccesor")
        if rootNode.leftchild is not None:
            #print("if", rootNode.leftchild.data)
            return self._minsuccesor(rootNode.leftchild)
        return rootNode

    def _get_last_node(self, node=None, parent=None):
        # Establece el nodo inicial como la raíz si no se proporciona
        if node == None:
            node = self
        # Si no tiene hijos, es el último nodo
        if not node.leftchild and not node.rightchild:
            return node, parent

        # Revisar primero el hijo derecho y luego el hijo izquierdo (para encontrar el último nodo)
        if node.rightchild:
            last_node, last_parent = node.rightchild._get_last_node(node.rightchild, node)
            if last_node:
                return last_node, last_parent

        if node.leftchild:
            last_node, last_parent = node.leftchild._get_last_node(node.leftchild, node)
            if last_node:
                return last_node, last_parent

        return None
    """
    def _get_last_node(self, node=None):
        # Establece el nodo inicial como la raíz si no se proporciona
        if node == None:
            node = self
        # Si no tiene hijos, es el último nodo
        if not node.leftchild and not node.rightchild:
            return node

        # Revisar primero el hijo derecho y luego el hijo izquierdo (para encontrar el último nodo)
        if node.rightchild:
            last_node = node.rightchild._get_last_node(node.rightchild)
            if last_node:
                return last_node

        if node.leftchild:
            last_node = node.leftchild._get_last_node(node.leftchild)
            if last_node:
                return last_node

        return None
    """
