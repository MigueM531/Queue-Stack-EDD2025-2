from class_queue import *
from class_stack import *

class Atraccion:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.visitantes = Stack() 

    def __str__(self):
        return f"{self.nombre} ({self.capacidad}/turno) -> {self.visitantes}"
    
class ParqueDiversiones:
    def __init__(self):
        self.atracciones = Queue() 
        self._inicializar_atracciones()

    def _inicializar_atracciones(self):
        self.atracciones.enqueue(Atraccion("Montaña Rusa", 3))
        self.atracciones.enqueue(Atraccion("Carros Chocones", 2))
        self.atracciones.enqueue(Atraccion("Rueda de la Fortuna", 2))
        self.atracciones.enqueue(Atraccion("Casa del Terror", 2))

