import requests
import time
from collections import Counter

url = "http://localhost/status"
num_requests = 100

print("Ejecutando prueba de carga...")
print("=" * 60)
responses = []
instances = []

for i in range(num_requests):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            responses.append("Success")
            data = response.json()
            instance = data.get("instance", "unknown")
            instances.append(instance)
        else:
            print(f"Request {i+1} failed with status {response.status_code}")
    except Exception as e:
        print(f"Request {i+1} error: {e}")
    if (i + 1) % 10 == 0:
        print(f"Progreso: {i + 1}/{num_requests} requests completados")

print("\n" + "=" * 60)
print("RESULTADOS DE LA PRUEBA")
print("=" * 60)
print(f"\nTotal requests exitosos: {len(responses)}/{num_requests}")

if len(instances) > 0:
    counter = Counter(instances)
    print(f"\nDISTRIBUCIÓN DE CARGA POR INSTANCIA:")
    print("-" * 60)
    for instance, count in counter.items():
        percentage = (count / len(instances)) * 100
        bar = "█" * int(percentage / 2)
        print(f"  {instance}: {count:3d} requests ({percentage:5.2f}%) {bar}")
    print("=" * 60)

if len(responses) == num_requests:
    print("✓ Prueba de carga completada correctamente.")
else:
    print("✗ Algunas solicitudes fallaron. Revisa la infraestructura y los logs.")