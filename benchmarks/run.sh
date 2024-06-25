#!/bin/bash
#python /src/main.py KNP --test /benchmarks/build/knp /instances/hardinstances_pisinger/knapPI_14_2000_1000_1.txt
#python /src/main.py TSP --test /benchmarks/build/tsp /instances/TSPLIB95/rat783.tsp
#python /src/main.py N_Queens --test /benchmarks/build/n_queens 14
#python /src/main.py MATRIX_MULT --test python /benchmarks/MATRIX_MULT/main.py 10000
python /src/main.py TSP2 --test /benchmarks/build/tsp /instances/TSPLIB95/u1060.tsp
python /src/main.py TSP3 --test /benchmarks/build/tsp /instances/TSPLIB95/u1817.tsp
python /src/main.py TSP4 --test /benchmarks/build/tsp /instances/TSPLIB95/u2319.tsp
python /src/main.py N_Queens2 /benchmarks/build/n_queens 15
python /src/main.py MATRIX_MULT2 python /benchmarks/MATRIX_MULT/main.py 15000
python /src/main.py MATRIX_MULT3 --test python /benchmarks/MATRIX_MULT/main.py 17500
