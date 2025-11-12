
# Examen Práctico: Sistemas Distribuidos

Este repositorio contiene la solución a dos partes del examen práctico:

## Parte 1: Procesamiento Distribuido (Procesos vs Hilos)

Ubicación: `PARTE1/task_processor.py`

### Instrucciones de ejecución
1. Tener Python 
2. Acceder a la carpeta `PARTE1`.      
   cd PARTE1
3. Ejecutar:

    python task_processor.py

4. Observar los resultados en consola: tiempos de ejecución y tareas completadas por hilos y procesos.

### Análisis de resultados
- Los hilos completan las tareas rápidamente cuando el trabajo es principalmente de espera.
- Los procesos pueden ser más lentos por el overhead de creación, pero aprovechan mejor los núcleos para tareas de CPU intensivo.
- El uso de `threading.Lock` evita condiciones de carrera en hilos.
- El contador compartido con `multiprocessing.Value` permite sincronización entre procesos.

### Conclusiones y conceptos aplicados
- **Procesos vs Hilos:** Usar hilos para tareas ligeras, procesos para tareas de CPU intensivo.
- **Comunicación entre procesos:** Se usa memoria compartida (`multiprocessing.Value`), pero tiene overhead.
- **Locks y sincronización:** Los locks son esenciales para evitar condiciones de carrera en hilos.
- **Memoria compartida:** Permite que los procesos actualicen un contador global.

------------------------------------

## Parte 2: Almacenamiento Distribuido con MongoDB y Docker

Ubicación: `PARTE2/distributed_storage.py` y `PARTE2/docker-compose.yml`

### Instrucciones de ejecución
1. Instalar Docker Desktop
2. Abrir la carpeta `PARTE2`.

   cd PARTE2   

3. Levantar los contenedores de MongoDB:
    ```powershell
    docker compose up -d
    ```
4. Ejecuta el script:
    ```powershell
    python distributed_storage.py
    ```
5. Observar la distribución de los documentos y la búsqueda distribuida en consola.

### Análisis de resultados
- Los documentos se distribuyen automáticamente entre los dos nodos de MongoDB.
- La búsqueda consulta ambos nodos y retorna el documento si existe.
- Las estadísticas muestran cuántos documentos hay en cada nodo, evidenciando la distribución.

### Conclusiones y conceptos aplicados
- **Almacenamiento distribuido:** Se logra sharding simple distribuyendo documentos entre nodos.
- **Consistencia:** La búsqueda consulta ambos nodos para garantizar la recuperación del documento.
- **Docker y contenedores:** Permiten levantar infraestructura distribuida de forma sencilla y replicable.

---

## Explicación de cómo se evitan condiciones de carrera
- En la parte de hilos, se usa `threading.Lock` para proteger el contador compartido.
- En la parte de procesos, se usa `multiprocessing.Value` para sincronizar el acceso al contador.
- En almacenamiento distribuido, cada nodo opera de forma independiente, evitando conflictos de concurrencia.

---

**Autor:** Steven Alexandre Mero Castro

