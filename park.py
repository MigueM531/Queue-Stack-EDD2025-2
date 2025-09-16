from class_queue import *
from class_stack import *

class Atraccion:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.visitantes = Stack() 

    def __str__(self):
        return f"{self.nombre} ({self.capacidad}/turno) -> {self.visitantes}"
    
