# Práctica: Sistema de Gestión de Parque de Diversiones (Cola de Pilas con Turnos de Procesamiento)

## Restricciones Técnicas
- Únicamente se pueden utilizar las clases de pilas y colas que fueron construidas en clase.  
- No se permite documentación sobre el código.  
- Únicamente se permite como colección de datos pilas/colas, es decir, **no se pueden utilizar listas, tuplas, diccionarios u otros**. Presentar la práctica sobre otra colección no cumple con lo solicitado (nota 0).  
- La práctica debe cumplir con la totalidad de los puntos solicitados; cada punto no presentado disminuirá la nota.  

---

## Descripción
Se debe implementar un sistema de gestión para un parque de diversiones, donde el flujo de las atracciones se organiza mediante **una cola de pilas**.  
Cada elemento de la cola representa una atracción del parque (ejemplo: Montaña Rusa, Carros Chocones, Rueda de la Fortuna, Casa del Terror).  
Dentro de cada atracción, los visitantes se organizan en **una pila (LIFO)**.

---

## Límites Iniciales por Atracción
- **Montaña Rusa** → Capacidad: 3 visitantes por turno  
- **Carros Chocones** → Capacidad: 2 visitantes por turno  
- **Rueda de la Fortuna** → Capacidad: 2 visitantes por turno  
- **Casa del Terror** → Capacidad: 2 visitantes por turno  

---

## Flujo del Sistema
1. **Ingreso de visitantes**: Se registran visitantes (adultos o niños) que entran al sistema y se agregan a la primera atracción de la cola (Montaña Rusa).  
2. **Procesamiento por turnos**:  
   - Cada atracción procesa hasta su capacidad máxima por turno.  
   - Los visitantes procesados pasan a la siguiente atracción en la cola.  
   - Los que no alcanzan a procesarse esperan en la pila de la atracción actual.  
3. **Ejecución de turnos**:  
   - Cada ejecución de turno debe mostrar un reporte indicando qué pasó en cada atracción.  
   - Esto continúa hasta que todos los visitantes salgan del sistema.  

---

## Reglas del Sistema
1. **Manejo de la cola de pilas**  
   - La cola de atracciones sigue un orden FIFO.  
   - Se pueden agregar o quitar atracciones.  
   - Si se elimina una atracción, los visitantes en su pila deben redistribuirse en las siguientes.  

2. **Manejo de las pilas de visitantes**  
   - Las pilas siguen un orden LIFO.  
   - Cada turno, la atracción procesa hasta su capacidad máxima.  
   - Los visitantes procesados se agregan en la pila de la siguiente atracción.  

3. **Ejecución de turnos**  
   - El sistema debe permitir ejecutar turnos de forma controlada.  
   - Puede implementarse con una opción en el menú "Ejecutar Turno", que muestre un reporte del movimiento de visitantes.  
   - Adicionalmente debe automatizarse con un ciclo que reporte cada turno hasta que todos los visitantes salgan del parque.  

---

## Operaciones Requeridas
1. **Agregar visitante al sistema (adulto o niño)**: Se registran visitantes y se agregan a la primera atracción de la cola (Montaña Rusa).  
2. **Procesar visitantes** en cada atracción según su límite de turno.  
3. **Ejecutar un turno**:  
   - Procesar las atracciones desde la primera hasta la última.  
   - Reportar qué visitantes fueron procesados en ese turno.  
   - Reportar qué visitantes quedaron en espera por turno.  
4. **Eliminar una atracción y redistribuir visitantes**.  
   - Ejemplo: Si la Rueda de la Fortuna se daña, los visitantes pasan directamente a la Casa del Terror.  
5. **Agregar una nueva atracción al flujo**.  
   - Ejemplo: Se activa promoción y se agrega una atracción Simulador 4D con límite de 2 visitantes por turno.  
6. **Consultar estado del sistema**:  
   - Mostrar cuántos visitantes están en cada atracción y en qué orden (en la pila).  

---

## Ejemplo de Escenario
1. Entran 7 visitantes: A1, N1, A2, N2, A3, A4, N3.  
2. Todos se agregan a la Montaña Rusa (capacidad 3 por turno).  
3. Se ejecuta el **Turno 1**:  
   - Montaña Rusa procesa 3 (los últimos de la pila).  
   - Carros Chocones aún vacío.  
   - Rueda de la Fortuna y Casa del Terror aún vacías.  

4. Se ejecuta el **Turno 2**:  
   - Montaña Rusa procesa 3 más.  
   - Carros Chocones procesa 2 de los 3 que recibió, en LIFO.  

5. Se ejecuta el **Turno 3**:  
   - Montaña Rusa procesa 1 visitante restante.  
   - Carros Chocones procesa 2 más.  
   - Rueda de la Fortuna procesa 2 de los procesados por Carros Chocones en el turno 2.  

El sistema sigue reportando turnos hasta que todos los visitantes hayan salido del parque.  

---

## Pistas de Implementación
- Cada atracción → una pila.  
- Cola principal → organiza las atracciones en orden.  

---

## Bonos Extras (Mayor Dificultad)
- **Implementación práctica con recursividad**: +0.5 adicional (depende de la sustentación oral).  
- **Modificación de 1 punto**: +0.5 adicional (depende de la sustentación oral).  

---

## Entrega y Sustentación
- **Fecha de entrega y sustentación**:  
  - 18 de septiembre durante clase (grupo martes y jueves).  
  - 19 de septiembre durante clase (grupo miércoles y viernes).  
- **Asistencia obligatoria**: Quien no asista tendrá nota 0 en sustentación práctica y 0.5 en implementación.  
- **Hora de envío**: Hasta las 6:15 am del día correspondiente.  
- **Trabajo individual o en parejas** (sustentación individual).  

### Evaluación
- Implementación: **20%**  
- Sustentación práctica: **40%** (de 6:00 am a 6:45 am en la fecha de entrega).  
- Sustentación oral: **40%** (de 6:45 am en adelante, ese día se indicará el orden).  
