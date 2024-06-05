#!/bin/bash
python /src/main.py KNP /benchmarks/build/knp /instances/hardinstances_pisinger/knapPI_14_2000_1000_1.txt
python /src/main.py N_Queens /benchmarks/build/n_queens 14
python /src/main.py TSP /benchmarks/build/tsp
python /src/main.py MATRIX_MULT python /benchmarks/MATRIX_MULT/main.py 10000
