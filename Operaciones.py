from datetime import *
from arbol import *
from Paquete import Paquete
import csv

class Operaciones:
    def __init__(self, maxsize):
        self.heap = HeapBinaryTree(maxsize)

    def registrar_paquete(self, prioridad: int, peso: float, tamano: int, destino: str, fecha_limite: date, llegada: date):
        if fecha_limite <= date.today():
            return "La fecha límite debe ser superior a la fecha actual."
        paquete = Paquete(prioridad, peso, tamano, destino, fecha_limite, llegada)
        resultado = self.heap.insert(paquete)
        return resultado

    def mostrar_heap(self):
        self.heap.printTree()

    def mostrar_heap_id(self):
        self.heap.printTreeIds()

    def mostar_en_lista(self):
        self.heap.inOrder() # No me funciona

    def imprimir_en_orden_prioridad(self):
        # Crear una copia temporal del heap para no alterar el original
        copia_heap = HeapBinaryTree(self.heap.maxsize)
        copia_heap.customlist = self.heap.customlist[:]
        copia_heap.lastindexused = self.heap.lastindexused

        print("Elementos en orden de prioridad:")
        print("-----------------")
        while copia_heap.lastindexused > 0:
            paquete = copia_heap.extract()
            print(paquete)
            print("-----------------")
        print("-----------------")

    def consultar_proximo_paquete(self):
        if self.heap.lastindexused == 0:
            return "No hay paquetes en el heap."
        return self.heap.customlist[1]

    def enviar_siguiente_paquete(self):
        if self.heap.lastindexused == 0:
            return "No hay paquetes en el heap."
        return self.heap.extract()

    def eliminar_paquete(self, identificador):
        if identificador is None:
            return "Debe proporcionar un identificador para eliminar el paquete."

        for i in range(1, self.heap.lastindexused + 1):
            paquete = self.heap.customlist[i]

            # si el id es igual al identificador se encontro el que se quiere elimianar
            if paquete.id == identificador:
                # se remplaza el nodo encontrado con el last(Ultimo del arbol)
                self.heap.customlist[i] = self.heap.customlist[self.heap.lastindexused]
                # Ese ultimo que se remplazo se pone en None
                self.heap.customlist[self.heap.lastindexused] = None
                # Se resta 1 para que se mantenga correctamente el tamaño del arbol
                self.heap.lastindexused -= 1
                # se usa el metodo para re organizar el arbol hasta que cumpla con el heapMin
                self.heap.heapify_down(i)

                return f"Paquete con ID {identificador} eliminado."

        return "Paquete no encontrado."

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
                    self.heap.insert(paquete)
                except (IndexError, ValueError) as e:
                    print(f"Error al procesar la fila {fila}: {e}")

        print("Paquetes cargados desde el archivo CSV.")

"""
# Ejemplo de uso
if __name__ == "__main__":
    operaciones = Operaciones(10)
    operaciones.registrar_paquete(0, 1.0, 0, "Bogotá", date(2024, 11, 30), date(2024, 11, 4))
    operaciones.registrar_paquete(0, 1.0, 0, "Medellín", date(2024, 11, 30), date(2024, 11, 3))
    operaciones.registrar_paquete(0, 1.0, 0, "Cali", date(2024, 11, 30), date(2024, 11, 4))

    operaciones.mostrar_heap()
    print("--------------------------")
    print("Próximo paquete a enviar:")
    print(operaciones.consultar_proximo_paquete())
    print("--------------------------")
    print("Enviando siguiente paquete:")
    print(operaciones.enviar_siguiente_paquete())
    print("--------------------------")
    operaciones.mostrar_heap()
    print("--------------------------")
    print("Eliminando paquete")
    operaciones.eliminar_paquete(3)
    print("--------------------------")

    operaciones.mostrar_heap()

"""

"""
from datetime import date
from arbol import HeapBinaryTree
from Paquete import Paquete

class Operaciones:
    def __init__(self, maxsize):
        self.heap = HeapBinaryTree(maxsize)

    def registrar_paquete(self, prioridad: int, peso: float, tamano: int, destino: str, fecha_limite: date, llegada: date):
        if fecha_limite <= date.today():
            return "La fecha límite debe ser superior a la fecha actual."
        paquete = Paquete(prioridad, peso, tamano, destino, fecha_limite, date.today())
        resultado = self.heap.insert(paquete)
        return resultado

    def mostrar_heap(self):
        self.heap.printTree()

    def consultar_proximo_paquete(self):
        if self.heap.lastindexused == 0:
            return "No hay paquetes en el heap."
        return self.heap.customlist[1]

# Ejemplo de uso
if __name__ == "__main__":
    operaciones = Operaciones(10)
    operaciones.registrar_paquete(0, 1.0, 0, "Bogotá", date(2024, 11, 30))
    operaciones.registrar_paquete(0, 1.0, 0, "Medellín", date(2024, 11, 30))
    operaciones.registrar_paquete(0, 1.0, 0, "Cali", date(2024, 11, 30))

    operaciones.mostrar_heap()
    print("--------------------------")
    print("Próximo paquete a enviar:")
    print(operaciones.consultar_proximo_paquete())
"""