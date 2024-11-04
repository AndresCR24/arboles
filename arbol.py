class HeapBinaryTree:
    def __init__(self, maxsize):
        self.customlist = [None] * (maxsize)  # Initialize list with max size
        self.maxsize = maxsize  # Max size of the heap
        self.lastindexused = 0  # Last used index

    def insert(self, data):
        if self.lastindexused + 1 >= self.maxsize:
            return "El arbol está lleno"

        # Insert in the first free space
        self.lastindexused += 1
        self.customlist[self.lastindexused] = data

        # Restore heap property (min-heap) by moving up
        self._heapify_up(self.lastindexused)
        return f"Nodo {data} insertado en el índice {self.lastindexused}"

    def _heapify_up(self, index):
        # Move the node up to maintain min-heap property
        parent_index = index // 2
        while parent_index > 0 and self.customlist[index] < self.customlist[parent_index]:
            # Swap if the current node is smaller than the parent node
            self.customlist[index], self.customlist[parent_index] = self.customlist[parent_index], self.customlist[
                index]
            index = parent_index
            parent_index = index // 2

    def heapify_down(self, index):
        # Move the node down to maintain min-heap property
        left_child_index = 2 * index
        right_child_index = 2 * index + 1
        smallest = index

        if left_child_index <= self.lastindexused and self.customlist[left_child_index] < self.customlist[smallest]:
            smallest = left_child_index
        if right_child_index <= self.lastindexused and self.customlist[right_child_index] < self.customlist[smallest]:
            smallest = right_child_index
        if smallest != index:
            self.customlist[index], self.customlist[smallest] = self.customlist[smallest], self.customlist[index]
            self.heapify_down(smallest)

    def extract(self):
        if self.lastindexused == 0:
            return "El arbol esta vacio"
        extracted_value = self.customlist[1]
        self.customlist[1] = self.customlist[self.lastindexused]
        self.customlist[self.lastindexused] = None
        self.lastindexused -= 1
        self.heapify_down(1)
        return extracted_value

    def printTree(self, index=1, prefix="", is_left=True):
        if index > self.lastindexused or self.customlist[index] is None:
            return

        # Recursive call for the right child
        if index * 2 + 1 <= self.lastindexused:
            self.printTree(index * 2 + 1, prefix + ("│   " if is_left else "    "), False)

        # Print the current node
        print(prefix + ("└── " if is_left else "┌── ") + str(self.customlist[index]))

        # Recursive call for the left child
        if index * 2 <= self.lastindexused:
            self.printTree(index * 2, prefix + ("    " if is_left else "│   "), True)

    def printTreeIds(self, index=1, prefix="", is_left=True):
        if index > self.lastindexused or self.customlist[index] is None:
            return

        # Recursive call for the right child
        if index * 2 + 1 <= self.lastindexused:
            self.printTreeIds(index * 2 + 1, prefix + ("│   " if is_left else "    "), False)

        # Print the ID of the current node
        print(prefix + ("└── " if is_left else "┌── ") + str(self.customlist[index].id))

        # Recursive call for the left child
        if index * 2 <= self.lastindexused:
            self.printTreeIds(index * 2, prefix + ("    " if is_left else "│   "), True)

    def inOrder(self, index=1):
        if index > self.lastindexused:
            return

        self.inOrder(index * 2)
        print(self.customlist[index])
        print("-----------------")
        self.inOrder(index * 2 + 1)

    def postOrder(self, index=1):
        if index > self.lastindexused:
            return
        self.postOrder(index * 2)
        self.postOrder(index * 2 + 1)
        print(self.customlist[index])
        print("-----------------")

"""
heap = MinHeap(10)  # Crear un min-heap con capacidad máxima de 10 elementos
heap.insert(2)
heap.insert(1)
heap.insert(2)
heap.insert(2)
heap.insert(2)
print(heap.insert(50))
print(heap.insert(30))
print(heap.insert(70))
print(heap.insert(20))
print(heap.insert(40))
print(heap.insert(60))
print(heap.insert(80))


heap.printTree()

"""

"""
class binarytree:

    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

    def __str__(self, level=0, index=1):
        ret = "  " * level + str(self.customlist[index]) + "\n"

        if index * 2 <= self.lastindexused:
            ret += self.__str__(level + 1, index * 2)
        if index * 2 + 1 <= self.lastindexused:
            ret += self.__str__(level + 1, index * 2 + 1)

        return ret

    def insert(self, data):

        if self.lastindexused + 1 >= self.maxsize:
            return "Arbol esta lleno"

        self.lastindexused += 1
        self.customlist[self.lastindexused] = data

    def preOrder(self, index=1):
        if index > self.lastindexused:
            return

        print(self.customlist[index])
        self.preOrder(index * 2)
        self.preOrder(index * 2 + 1)

    def inOrder(self, index=1):
        if index > self.lastindexused:
            return

        self.inOrder(index * 2)
        print(self.customlist[index])
        self.inOrder(index * 2 + 1)

    def postOrder(self, index=1):
        if index > self.lastindexused:
            return

        self.postOrder(index * 2)
        self.postOrder(index * 2 + 1)
        print(self.customlist[index])

    def levelOrder(self):

        for i in range(1, self.lastindexused + 1):
            print(self.customlist[i])

    def searchNode(self, value):

        for i in range(1, self.lastindexused + 1):
            if self.customlist[i] == value:
                return "El nodo con valor {} fue encontrado".format(value)

        return "El nodo con valor {} NO fue encontrado".format(value)


def printTree(Node, prefix="", is_left=True):
    if not Node:
        return

    if Node.rightchild:
        printTree(Node.rightchild, prefix + ("│    " if is_left else "    "), False)

    print(prefix + ("└── " if is_left else "┌── ") + str(Node.data))

    if Node.leftchild:
        printTree(Node.leftchild, prefix + ("     " if is_left else "│   "), True)


def count_leaves(rootNode, value):
    if rootNode is None:
        return 0

    contador = 0
    if rootNode.leftchild is None and rootNode.rightchild is None:
        if rootNode.data == value:
            return 1

    if rootNode.leftchild is not None:
        contador += count_leaves(rootNode.leftchild, value)

    if rootNode.rightchild is not None:
        contador += count_leaves(rootNode.rightchild, value)

    return contador
"""
