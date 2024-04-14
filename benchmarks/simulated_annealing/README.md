# Instrucciones de ejecución

- Compilar programa:
```bash
make
```

- Ejecutar programa:
```bash
./sa_bench <instancia> <q> <tmax> <qt> <qm>
```

- instancia: es la ruta del archivo .txt que contiene la instancia del problema a evaluar.
- q: Temperatura inicial.
- tmax: Maxima cantidad de iteracioneso
- qt: Velocidad de cambio de temperatura.
- qm: Magnitud de cambio de temperatura.

Ejemplo:
```bash
./sa_bench instancia/InstanceBEP-1-4-2-4.txt 100 1000 1 5
```

- Limpiar archivos de compilado y ejecutable:
```bash
make clean
```

# Datos adicionales del Output
Se imprime el tiempo de evacuación conseguido en la Solución inicial, como comparación con el resultado final conseguido por Simulated Annealing.

