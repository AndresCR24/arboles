import sys
from datetime import date
from Operaciones2 import Operaciones2  # Asegúrate de que el nombre del archivo es correcto

class Menu2:
    def __init__(self):
        self.operaciones = Operaciones2()

    def mostrar_menu(self):
        print("\n--- Menú de Paquetes ---")
        print("1. Registrar paquete")
        print("2. Mostrar Paquetes")
        print("3. Consultar próximo paquete")
        print("4. Enviar siguiente paquete")
        print("5. Eliminar paquete")
        print("6. Mostrar paquetes por ID")
        print("7. Mostrar paquetes en lista")
        print("10. Cargar paquetes desde archivo CSV")
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
                self.mostrar_en_lista()
            elif opcion == "10":
                archivo_csv = input("Ingrese el nombre del archivo CSV: ")
                self.operaciones.cargar_paquetes_desde_csv(archivo_csv)
            elif opcion == "0":
                print("Saliendo...")
                sys.exit()
            else:
                print("Opción no válida. Intente de nuevo.")

    def registrar_paquete(self):
        try:
            prioridad = int(input("Ingrese la prioridad (0 máxima prioridad, hasta 4 mínima prioridad): "))
            peso = float(input("Ingrese el peso: "))
            tamano = int(input("Ingrese el tamaño (0: Grande, 1: Mediano, 2: Pequeño): "))
            destino = input("Ingrese el destino: ")
            fecha_limite_input = input("Ingrese la fecha límite (YYYY-MM-DD): ")
            llegada_input = input("Ingrese la fecha de llegada (YYYY-MM-DD): ")

            fecha_limite = date.fromisoformat(fecha_limite_input) if fecha_limite_input else None
            llegada = date.fromisoformat(llegada_input) if llegada_input else None

            resultado = self.operaciones.registrar_paquete(prioridad, peso, tamano, destino, fecha_limite, llegada)
            print(resultado)
        except ValueError as e:
            print(f"Error en la entrada de datos: {e}")

    def mostrar_heap(self):
        self.operaciones.mostrar_heap()

    def mostrar_heap_id(self):
        self.operaciones.mostrar_heap_id()

    def mostrar_en_lista(self):
        self.operaciones.mostar_en_lista()

    def consultar_proximo_paquete(self):
        paquete = self.operaciones.consultar_proximo_paquete()
        if isinstance(paquete, str):
            print(paquete)
        else:
            print(paquete)

    def enviar_siguiente_paquete(self):
        paquete = self.operaciones.enviar_siguiente_paquete()
        if isinstance(paquete, str):
            print(paquete)
        else:
            print("Paquete enviado:")
            print(paquete)

    def eliminar_paquete(self):
        try:
            identificador = int(input("Ingrese el ID del paquete a eliminar: "))
            resultado = self.operaciones.eliminar_paquete(identificador)
            print(resultado)
        except ValueError:
            print("El ID debe ser un número entero.")


