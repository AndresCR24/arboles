from datetime import date


class Paquete:
    id_paquete = 1
    tamano = ["Grande", "Mediano", "Pequeño"]
    prioridad = [1, 2, 3, 4, 5]

    def __init__(self, prioridad: int, peso: float, tamano: int, destino: str = "", fecha_limite: date = None,
                 llegada: date = None):
        self.id = Paquete.id_paquete
        Paquete.id_paquete += 1
        self.prioridad = Paquete.prioridad[prioridad]  # Un valor específico para cada paquete, entre 1 y 5
        self.peso = peso
        self.tamano = Paquete.tamano[tamano]  # Puede ser "Grande", "Mediano", "Pequeño"
        self.destino = destino
        self.fecha_limite = fecha_limite
        self.llegada = llegada  # Fecha de llegada (orden de llegada)

    def __lt__(self, other):
        if self.peso != other.peso:
            return self.peso < other.peso
        if self.llegada != other.llegada:
            return self.llegada < other.llegada
        # if self.fecha_limite != other.fecha_limite:
        #    return self.fecha_limite < other.fecha_limite
        if self.tamano != other.tamano:
            return self.tamano < other.tamano
        return self.prioridad < other.prioridad


    def __str__(self):
        return (f"Paquete ID: {self.id}\n"
                f"Prioridad: {self.prioridad}\n"
                f"Peso: {self.peso} kg\n"
                f"Tamaño: {self.tamano}\n"
                f"Destino: {self.destino}\n"
                f"Fecha límite: {self.fecha_limite}\n"
                f"Fecha de llegada: {self.llegada}")

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __ne__(self, other):
        return not self == other
    """
    def __lt__(self, other):
        if self.prioridad != other.prioridad:
            return self.prioridad < other.prioridad
        if self.fecha_limite != other.fecha_limite:
            return self.fecha_limite < other.fecha_limite
        if self.peso != other.peso:
            return self.peso < other.peso
        if self.tamano != other.tamano:
            return self.tamano < other.tamano
        return self.llegada < other.llegada
    """


"""
    def __lt__(self, other):
        return self.id < other.id

    def __le__(self, other):
        return self.id <= other.id

    def __gt__(self, other):
        return self.id > other.id

    def __ge__(self, other):
        return self.id >= other.id

    def __ne__(self, other):
        return self.id != other.id
"""

"""
# Ejemplo de uso
paquete1 = Paquete(1, 2.5, 0)  # 0 corresponde a "Grande"
paquete2 = Paquete(2, 3.0, 1, "Medellín", date(2024, 11, 30), date(2024, 12, 10))  # 1 corresponde a "Mediano"
paquete3 = Paquete(4, 5, 2)  # 2 corresponde a "Pequeño"

print(paquete1)
print("------------------")
print(paquete2)
print("------------------")
print(paquete3)
"""
