# resource-prediction-study
Este repositorio contiene el código y *benchmarks* utilizados en el estudio **Modelo de Predicción de Consumo de Rercursos Computacionales**.

## Descripción
El estudio tiene como objetivo principal la creación de un modelo de predicción de consumo de recursos computacionales en una máquina objetivo a partir del consumo de recursos y características de una máquina base. 

Para ello, se ha utilizado un conjunto de datos de trazas de ejecución de contenedores. El modelo de predicción se ha creado utilizando técnicas de aprendizaje automático y se ha evaluado su rendimiento en términos de precisión y eficiencia.

## Benchmarks
Los benchmarks utilizados en el estudio son los siguientes:
- Simulated Annealing
- SQL Join
- Matrix Multiplication

## Dependencias
- [apptainer](https://apptainer.org/) o [Docker](https://www.docker.com/)

## Apptainer
### Build de contenedor con apptainer
```bash
apptainer build new_container.sif apptainer.def
```

### Ejecución de benchmarks
```bash
apptainer run new_container.sif
```

## Docker
### Build de contenedor con Docker
```bash
docker build -t new_container .
```

### Ejecución de benchmarks
```bash
docker run -it -v ./results:/results new_container
```

## Descripción de los benchmarks
### Simulated Annealing
Resuelve el problema *Bus Evacuation Problem* (BEP) usando el algoritmo de *Simulated Annealing*, dado una instancia del problema.

### SQL Join
Realiza una operación de *join* entre dos tablas de una base de datos SQL, dado un conjunto de parámetros de entrada.

### Matrix Multiplication
Realiza la multiplicación de dos matrices cuadradas de tamaño *n x n*, dado un valor de *n*.

## Métricas de evaluación
Las métricas de evaluación utilizadas en el estudio son las siguientes:
- strace:
  - Llamadas al sistema
- time:
  - Tiempo de ejecución
  - Porcentaje de CPU utilizado
  - Máximo uso de RAM
  - Cantidad de veces que el proceso fue intercambiado hacia afuera de la RAM
- callgrind:
  - Ir: lecturas de caché (intrucciones ejecutadas)
  - I1mr: I1 lecturas perdidas de caché (intrucciones que no se encuentran en la caché I1 pero se encuentran en la L2)
  - I2mr: L2 lecturas perdidas de caché (intrucciones que no se encuentran en la caché I1 o L2 pero se encuentran en la RAM)
  - Dr: D lecturas de caché (lecturas de memoria)
  - D1mr: D1 lecturas perdidas de caché (Ubicación de datos no encontrada en D1, pero encontrada en L2)
  - D2mr: L2 lecturas perdidas de datos caché (Ubicación de datos no encontrada en D1 o L2)
  - Dw: D escrituras de caché (escrituras de memoria)
  - D1mw: D1 escrituras perdidas de caché (Ubicación de datos no encontrada en D1, pero encontrada en L2)
  - D2mw: L2 escrituras perdidas de caché (Ubicación de datos no encontrada en D1 o L2)
- Registrados en ejecución:
  - Uso de CPU
  - Uso de memoria

Además, se recopila la información disponible del sistema como:
- Arquitectura
- Nombre de la CPU
- Frecuencia de la CPU
- Tamaño de cache L2 de CPU
- Tamaño de cache L3 de CPU
- Tamaño total de RAM