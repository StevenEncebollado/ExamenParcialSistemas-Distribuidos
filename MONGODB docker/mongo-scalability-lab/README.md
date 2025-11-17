# Despliegue Escalable: MongoDB en Contenedores con Balanceo de Carga

## Objetivo de la Práctica
Implementar una infraestructura básica escalable usando MongoDB en Docker y demostrar cómo distribuir la carga entre múltiples instancias.

## Tareas a Realizar
1. Configurar Infraestructura en Docker
   - Desplegar 3 contenedores de MongoDB
   - Crear una red Docker para comunicación
   - Configurar una aplicación web simple que se conecte a MongoDB
   - Implementar un balanceador de carga (Nginx)
   
2. Simular Escalabilidad
   - Probar que la aplicación funcione con una instancia
   - Escalar a múltiples instancias de MongoDB
   - Demostrar distribución de carga
   - Simular alta demanda


## Instrucciones Paso a Paso

### Paso 1: Clonar y Preparar el Entorno
```bash
# Clonar el repositorio
git clone https://github.com/StevenEncebollado/ExamenParcialSistemas-Distribuidos.git

# Entrar al directorio del proyecto
cd mongo-scalability-lab

# Verificar que Docker esté instalado y ejecutándose
docker --version
docker-compose --version
```
**IMPORTANTE**: Docker Desktop debe estar ejecutándose antes de continuar.

### Paso 2: Desplegar la Infraestructura
```powershel
# 1. Accede a la ruta del proyecto
cd mongo-scalability-lab

# 2. Levanta todos los servicios
docker-compose -f docker/docker-compose.yml up -d

# 3. Verificar que todo esté funcionando
docker ps
```
Contenedores que deberían estar corriendo:
- `mongo1` (puerto 27017)
- `mongo2` (puerto 27018)
- `mongo3` (puerto 27019)
- `docker-webapp-1` (puerto 5000)
- `docker-load-balancer-1` (puerto 80)

### Paso 3: Probar la Aplicación
```bash
# Probar la aplicación directamente (Windows PowerShell)
curl http://localhost:5000

# Probar a través del balanceador de carga
curl http://localhost:80

**Resultado esperado**: "Aplicación Escalable con MongoDB!"

### Paso 4: Ejecutar Pruebas de Carga
```powershell

# 1. Ejecuta el script de pruebas
python scripts/load_test.py
```
El script mostrará el progreso cada 10 solicitudes y al final:

```
Ejecutando prueba de carga...
Progreso: 10/100 requests completados
Progreso: 20/100 requests completados
...
Total requests exitosos: 100/100
Prueba de carga completada correctamente.
```