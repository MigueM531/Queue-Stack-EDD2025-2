from class_queue import *
from class_stack import *

class Atraccion:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.visitantes = Stack() 

    def agregar_visitante(self, visitante):
        self.visitantes.push(visitante)
    
    def procesar_turno(self):
        procesados = Queue()
        for _ in range(self.capacidad):
            if not self.visitantes.is_empty():
                procesados.enqueue(self.visitantes.pop())
        return procesados  

    def __str__(self):
        return f"{self.nombre} (capacidad: {self.capacidad}) -> {self.visitantes}"
    
class ParqueDiversiones:
    def __init__(self):
        self.atracciones = Queue() 

        self.atracciones.enqueue(Atraccion("Montaña Rusa", 3))
        self.atracciones.enqueue(Atraccion("Carros Chocones", 2))
        self.atracciones.enqueue(Atraccion("Rueda de la Fortuna", 2))
        self.atracciones.enqueue(Atraccion("Casa del Terror", 2))

    def agregar_visitante(self, visitante):
        primera_atraccion = self.atracciones.first()
        primera_atraccion.visitantes.push(visitante)

    def ejecutar_turno(self):
        procesados_siguiente = Queue()
        nueva_cola = Queue()

        while not self.atracciones.is_empty():
            atraccion = self.atracciones.dequeue()

            while not procesados_siguiente.is_empty():
                atraccion.agregar_visitante(procesados_siguiente.dequeue())

            procesados = atraccion.procesar_turno()
            procesados_siguiente = procesados

            print(f"{atraccion.nombre} -> Procesados: {procesados}, "
                  f"En espera: {atraccion.visitantes}")

            nueva_cola.enqueue(atraccion)

        self.atracciones = nueva_cola


    def estado(self):
        cola_temporal = Queue()

        while not self.atracciones.is_empty():
            atraccion = self.atracciones.dequeue()
            print(atraccion)
            cola_temporal.enqueue(atraccion)

        while not cola_temporal.is_empty():
            self.atracciones.enqueue(cola_temporal.dequeue())

    
    def eliminar_atraccion(self, nombre):
        nueva_cola = Queue()
        visitantes_temp = Stack()
        while not self.atracciones.is_empty():
            atraccion = self.atracciones.dequeue()
            if atraccion.nombre == nombre:
                while not atraccion.visitantes.is_empty():
                    visitantes_temp.push(atraccion.visitantes.pop())
            else:
                nueva_cola.enqueue(atraccion)
    
        if not visitantes_temp and nueva_cola.is_empty():
            return
        siguiente = nueva_cola.first()
        while not visitantes_temp.is_empty():
            siguiente.visitantes.push(visitantes_temp.pop())
        self.atracciones = nueva_cola

    def agregar_atraccion(self, nombre, capacidad):
        self.atracciones.enqueue(Atraccion(nombre, capacidad))



def prueba_escenario():
    parque = ParqueDiversiones()

    visitantes = Queue()
    visitantes.enqueue("A1")
    visitantes.enqueue("N1")
    visitantes.enqueue("A2")
    visitantes.enqueue("N2")
    visitantes.enqueue("A3")
    visitantes.enqueue("A4")
    visitantes.enqueue("N3")

    while not visitantes.is_empty():
        parque.agregar_visitante(visitantes.dequeue())

    print("-----------------------------------------------------------")
    print("Estado inicial del parque:")
    parque.estado()
    print("-----------------------------------------------------------")

    turno = 1

    while True:
        print(f"--- Turno {turno} ---")
        parque.ejecutar_turno()
        print("Estado después del turno:")
        parque.estado()
        print("-----------------------------------------------------------")
        
        todas_vacias = True
        colatemp = Queue()

        if turno == 2:
          print("PROMOCIÓN (SE AGREGÓ UNA NUEVA ATRACCIÓN AL PARQUE)")
          parque.atracciones.enqueue(Atraccion("Simulador 4D", 2))

        if turno == 3:
          print("SE AVERIÓ UNA ATRACCIÓN (RUEDA DE LA FORTUNA)")
          parque.eliminar_atraccion("Rueda de la Fortuna")

        while not parque.atracciones.is_empty():
            atraccion = parque.atracciones.dequeue()
            if not atraccion.visitantes.is_empty():
                todas_vacias = False
            colatemp.enqueue(atraccion)

        while not colatemp.is_empty():
            parque.atracciones.enqueue(colatemp.dequeue())

        if todas_vacias == True:
            print("Todos los visitantes han salido del parque.")
            break

        turno += 1

prueba_escenario()