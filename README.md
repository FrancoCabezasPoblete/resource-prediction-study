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
- (apptainer)[https://apptainer.org/]

## Build de contenedor
```bash
apptainer build new_container.sif apptainer.def
```

## Ejecución de benchmarks
```bash
apptainer run new_container.sif
```

## Descrición de los benchmarks
### Simulated Annealing
Resuelve el problema *Bus Evacuation Problem* (BEP) usando el algoritmo de *Simulated Annealing*, dado una instancia del problema.

### SQL Join
Realiza una operación de *join* entre dos tablas de una base de datos SQL, dado un conjunto de parámetros de entrada.

### Matrix Multiplication
Realiza la multiplicación de dos matrices cuadradas de tamaño *n x n*, dado un valor de *n*.
