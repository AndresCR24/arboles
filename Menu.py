import sys
from datetime import date
from Operaciones import Operaciones

class Menu:
    def __init__(self):
        self.operaciones = Operaciones(10)

    def mostrar_menu(self):
        print("\n--- Menú de Paquetes ---")
        print("1. Registrar paquete")
        print("2. Mostrar Paquetes")
        print("3. Consultar próximo paquete")
        print("4. Enviar siguiente paquete")
        print("5. Eliminar paquete")
        print("6. Mostar paquetes por id")
        print("7. Mostar paquetes en lista")
        print("10. Cargar salas desde archivo CSV")
        print("0. Salir")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.registrar_paquete()
            elif opcion == "2":
                self.mostrar_heap()
            elif opcion == "3":
                self.consultar_proximo_paquete()
            elif opcion == "4":
                self.enviar_siguiente_paquete()
            elif opcion == "5":
                self.eliminar_paquete()
            elif opcion == "6":
                self.mostrar_heap_id()
            elif opcion == "7":
                self.operaciones.imprimir_en_orden_prioridad()
            elif opcion == "10":
                archivo_csv = input("Ingrese el nombre del archivo CSV: ")
                self.operaciones.cargar_paquetes_desde_csv(archivo_csv)
            elif opcion == "0":
                print("Saliendo...")
                sys.exit()
            else:
                print("Opción no válida. Intente de nuevo.")

    def registrar_paquete(self):
        prioridad = int(input("Ingrese la prioridad (0-4): "))
        peso = float(input("Ingrese el peso: "))
        tamano = int(input("Ingrese el tamaño (0: Grande, 1: Mediano, 2: Pequeño): "))
        destino = input("Ingrese el destino: ")
        fecha_limite = date.fromisoformat(input("Ingrese la fecha límite (YYYY-MM-DD): "))
        llegada = date.fromisoformat(input("Ingrese la fecha de llegada (YYYY-MM-DD): "))
        resultado = self.operaciones.registrar_paquete(prioridad, peso, tamano, destino, fecha_limite, llegada)
        print(resultado)

    def mostrar_heap(self):
        self.operaciones.mostrar_heap()

    def mostrar_heap_id(self):
        self.operaciones.mostrar_heap_id()
    def consultar_proximo_paquete(self):
        print(self.operaciones.consultar_proximo_paquete())

    def enviar_siguiente_paquete(self):
        print(self.operaciones.enviar_siguiente_paquete())

    def eliminar_paquete(self):
        identificador = int(input("Ingrese el ID del paquete a eliminar: "))
        print(self.operaciones.eliminar_paquete(identificador))
