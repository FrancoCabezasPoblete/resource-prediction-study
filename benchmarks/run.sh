#!/bin/bash
python /src/main.py KNP --val /benchmarks/build/knp
python /src/main.py N_Queens --val /benchmarks/build/n_queens 14
python /src/main.py TSP --val /benchmarks/build/tsp
python /src/main.py MATRIX_MULT --val python /benchmarks/MATRIX_MULT/main.py 5000
