import multiprocessing
import threading
import time
import random

# Función global para procesamiento de tarea
def process_task_global(task_id, difficulty):
    print(f"Procesando tarea {task_id} con dificultad {difficulty}")
    time.sleep(difficulty * 0.2)

# Función global para worker de procesos
def process_worker_global(task_id, difficulty, counter):
    process_task_global(task_id, difficulty)
    counter.value += 1

class TaskProcessor:
    def __init__(self):
        self.tasks_completed = multiprocessing.Value('i', 0)
        self.lock = threading.Lock()  # Para hilos

    def process_task(self, task_id, difficulty):
        process_task_global(task_id, difficulty)

    def thread_worker(self, task_id, difficulty):
        self.process_task(task_id, difficulty)
        with self.lock:
            self.tasks_completed.value += 1

    def run_with_threads(self, tasks):
        threads = []
        self.tasks_completed.value = 0
        start = time.time()
        for tid, diff in tasks:
            t = threading.Thread(target=self.thread_worker, args=(tid, diff))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        end = time.time()
        print(f"Threads completaron {self.tasks_completed.value} tareas en {end-start:.2f} segundos")

    def run_with_processes(self, tasks):
        processes = []
        self.tasks_completed.value = 0
        start = time.time()
        for tid, diff in tasks:
            p = multiprocessing.Process(target=process_worker_global, args=(tid, diff, self.tasks_completed))
            processes.append(p)
            p.start()
        for p in processes:
            p.join()
        end = time.time()
        print(f"Procesos completaron {self.tasks_completed.value} tareas en {end-start:.2f} segundos")

if __name__ == "__main__":
    tp = TaskProcessor()
    tareas = [(i, random.randint(1,5)) for i in range(20)]
    print("Ejecutando con hilos...")
    tp.run_with_threads(tareas)
    print("\nEjecutando con procesos...")
    tp.run_with_processes(tareas)
