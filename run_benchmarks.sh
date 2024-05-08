#!/bin/bash
python /src/main.py matrix_multiplication python /benchmarks/matrix_multiplication/main.py 5000
python /src/main.py sql_join python /benchmarks/sql_join/main.py /src/example.db
python /src/main.py simulated_annealing /benchmarks/simulated_annealing/sa_bench $SA_INSTANCES/InstanceBEP-8-40-20-20.txt 100 1000 1 5