from datetime import *
from arbol2 import *
from Paquete import Paquete
import csv

class Operaciones2:
    def __init__(self):
        self.heap = None

    def registrar_paquete(self, prioridad: int, peso: float, tamano: int, destino: str, fecha_limite: date, llegada: date):
        if fecha_limite <= date.today():
            return "La fecha límite debe ser superior a la fecha actual."
        paquete = Paquete(prioridad, peso, tamano, destino, fecha_limite, llegada)
        if self.heap is None:
            self.heap = MinHeapBinaryTree(paquete)
        else:
            self.heap.insert(paquete)
        return "Paquete registrado correctamente."

    def mostrar_heap(self):
        if self.heap and self.heap.data:
            self.heap.printTree()
        else:
            print("El arbol está vacío.")

    def mostrar_heap_id(self):
        if self.heap and self.heap.data:
            self.heap.printTreeIds()
        else:
            print("El arbol está vacío.")

    def mostar_en_lista(self):
        if self.heap and self.heap.data:
            self.heap.inOrder()
        else:
            print("El arbol está vacío.")

    def consultar_proximo_paquete(self):
        if self.heap is None or self.heap.data is None:
            return "No hay paquetes"
        return self.heap.data

    def enviar_siguiente_paquete(self):
        if self.heap is None or self.heap.data is None:
            return "No hay paquetes."
        paquete = self.heap.extractRoot()
        if self.heap.data is None:
            self.heap = None  # El heap está vacío ahora
        return paquete

    def eliminar_paquete(self, identificador):
        if identificador is None:
            return "Debe proporcionar un identificador para eliminar el paquete."

        if self.heap is None or self.heap.data is None:
            return "No hay paquetes."

        deleted = self.heap.deleteNode(identificador)

        if deleted:
            if self.heap.data is None:
                #Colocar en none para eliminar la referencia
                self.heap = None
            return f"Paquete con ID {identificador} eliminado."
        else:
            return "el paquete no fue encontrado."


    def cargar_paquetes_desde_csv(self, archivo_csv):
        with open(archivo_csv, mode='r') as file:
            reader = csv.reader(file)
            for fila in reader:
                try:
                    # Asume que las columnas están en el siguiente orden en el CSV:
                    # prioridad, peso, tamaño, destino, fecha_limite, llegada
                    prioridad = int(fila[0])  # Índice de prioridad (0-4)
                    peso = float(fila[1])  # Peso del paquete
                    tamano = int(fila[2])  # Índice de tamaño (0-2)
                    destino = fila[3]  # Destino como string
                    fecha_limite = datetime.strptime(fila[4], '%Y-%m-%d').date() if fila[4] else None
                    llegada = datetime.strptime(fila[5], '%Y-%m-%d').date() if fila[5] else None

                    # Verificar que la fecha límite sea válida
                    if fecha_limite and fecha_limite <= date.today():
                        print(
                            f"La fecha límite para el paquete con destino {destino} debe ser superior a la fecha actual.")
                        continue

                    paquete = Paquete(prioridad, peso, tamano, destino, fecha_limite, llegada)
                    if self.heap is None:
                        self.heap = MinHeapBinaryTree(paquete)
                    else:
                        self.heap.insert(paquete)
                except (IndexError, ValueError) as e:
                    print(f"Error al procesar la fila {fila}: {e}")

        print("Paquetes cargados desde el archivo CSV.")