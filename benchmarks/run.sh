#!/bin/bash
python /src/main.py KNP --test --sys /benchmarks/build/knp /instances/hardinstances_pisinger/knapPI_14_2000_1000_1.txt
# KNP<filename>
python /src/main.py KNPS_FILE_1_500_1000 --test --sys /benchmarks/build/knps_file /instances/smallcoeff_pisinger/knapPI_1_500_1000.csv
python /src/main.py KNPS_FILE_1_500_10000 --test --sys /benchmarks/build/knps_file /instances/smallcoeff_pisinger/knapPI_1_500_10000.csv
python /src/main.py KNPS_FILE_1_1000_1000 --test --sys /benchmarks/build/knps_file /instances/smallcoeff_pisinger/knapPI_1_1000_1000.csv
python /src/main.py KNPS_FILE_1_1000_10000 --test --sys /benchmarks/build/knps_file /instances/smallcoeff_pisinger/knapPI_1_1000_10000.csv
python /src/main.py KNPS_FILE_1_2000_1000 --test --sys /benchmarks/build/knps_file /instances/smallcoeff_pisinger/knapPI_1_2000_1000.csv
python /src/main.py KNPS_FILE_1_2000_10000 --test --sys /benchmarks/build/knps_file /instances/smallcoeff_pisinger/knapPI_1_2000_10000.csv
python /src/main.py KNPS_FILE_1_5000_1000 --test --sys /benchmarks/build/knps_file /instances/smallcoeff_pisinger/knapPI_1_5000_1000.csv
python /src/main.py KNPS_FILE_1_5000_10000 --test --sys /benchmarks/build/knps_file /instances/smallcoeff_pisinger/knapPI_1_5000_10000.csv
python /src/main.py KNPS_FILE_1_10000_1000 --test --sys /benchmarks/build/knps_file /instances/smallcoeff_pisinger/knapPI_1_10000_1000.csv
python /src/main.py KNPS_FILE_1_10000_10000 --test --sys /benchmarks/build/knps_file /instances/smallcoeff_pisinger/knapPI_1_10000_10000.csv
python /src/main.py KNPS_FILE_2_500_1000 --test --sys /benchmarks/build/knps_file /instances/smallcoeff_pisinger/knapPI_2_500_1000.csv
python /src/main.py KNPS_FILE_2_500_10000 --test --sys /benchmarks/build/knps_file /instances/smallcoeff_pisinger/knapPI_2_500_10000.csv
python /src/main.py KNPS_FILE_2_1000_1000 --test --sys /benchmarks/build/knps_file /instances/smallcoeff_pisinger/knapPI_2_1000_1000.csv
python /src/main.py KNPS_FILE_2_1000_10000 --test --sys /benchmarks/build/knps_file /instances/smallcoeff_pisinger/knapPI_2_1000_10000.csv
python /src/main.py KNPS_FILE_2_2000_1000 --test --sys /benchmarks/build/knps_file /instances/smallcoeff_pisinger/knapPI_2_2000_1000.csv
python /src/main.py KNPS_FILE_2_2000_10000 --test --sys /benchmarks/build/knps_file /instances/smallcoeff_pisinger/knapPI_2_2000_10000.csv
python /src/main.py KNPS_FILE_2_5000_1000 --test --sys /benchmarks/build/knps_file /instances/smallcoeff_pisinger/knapPI_2_5000_1000.csv
python /src/main.py KNPS_FILE_2_5000_10000 --test --sys /benchmarks/build/knps_file /instances/smallcoeff_pisinger/knapPI_2_5000_10000.csv
python /src/main.py KNPS_FILE_3_50_1000 --test --sys /benchmarks/build/knps_file /instances/smallcoeff_pisinger/knapPI_3_50_1000.csv
python /src/main.py KNPS_FILE_3_50_10000 --test --sys /benchmarks/build/knps_file /instances/smallcoeff_pisinger/knapPI_3_50_10000.csv
python /src/main.py KNPS_FILE_4_50_1000 --test --sys /benchmarks/build/knps_file /instances/smallcoeff_pisinger/knapPI_4_50_1000.csv
python /src/main.py KNPS_FILE_4_50_10000 --test --sys /benchmarks/build/knps_file /instances/smallcoeff_pisinger/knapPI_4_50_10000.csv
python /src/main.py KNPS_FILE_5_50_1000 --test --sys /benchmarks/build/knps_file /instances/smallcoeff_pisinger/knapPI_5_50_1000.csv
python /src/main.py KNPS_FILE_5_50_10000 --test --sys /benchmarks/build/knps_file /instances/smallcoeff_pisinger/knapPI_5_50_10000.csv

python /src/main.py KNPS_FILE_12_20_1000 --test --sys /benchmarks/build/knps_file /instances/hardinstances_pisinger/knapPI_12_20_1000.csv
python /src/main.py KNPS_FILE_13_20_1000 --test --sys /benchmarks/build/knps_file /instances/hardinstances_pisinger/knapPI_13_20_1000.csv
python /src/main.py KNPS_FILE_14_50_1000 --test --sys /benchmarks/build/knps_file /instances/hardinstances_pisinger/knapPI_14_50_1000.csv
python /src/main.py KNPS_FILE_15_50_1000 --test --sys /benchmarks/build/knps_file /instances/hardinstances_pisinger/knapPI_15_50_1000.csv
python /src/main.py KNPS_FILE_16_50_1000 --test --sys /benchmarks/build/knps_file /instances/hardinstances_pisinger/knapPI_16_50_1000.csv

# TSP
python /src/main.py TSP --test --sys /benchmarks/build/tsp /instances/TSPLIB95/rat783.tsp
python /src/main.py TSP2 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/u1060.tsp
python /src/main.py TSP3 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/u1817.tsp
python /src/main.py TSP4 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/u2319.tsp
# TSP<filename>
python /src/main.py TSPd198 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/d198.tsp
python /src/main.py TSPd493 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/d493.tsp
python /src/main.py TSPd657 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/d657.tsp
python /src/main.py TSPd1291 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/d1291.tsp
python /src/main.py TSPd1655 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/d1655.tsp
python /src/main.py TSPd2103 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/d2103.tsp
python /src/main.py TSPfl417 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/fl417.tsp
python /src/main.py TSPfl1400 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/fl1400.tsp
python /src/main.py TSPfl1577 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/fl1577.tsp
python /src/main.py TSPfl3795 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/fl3795.tsp
python /src/main.py TSPgil262 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/gil262.tsp
python /src/main.py TSPkroA150 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/kroA150.tsp
python /src/main.py TSPkroA200 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/kroA200.tsp
python /src/main.py TSPkroB150 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/kroB150.tsp
python /src/main.py TSPkroB200 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/kroB200.tsp
python /src/main.py TSPlin105 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/lin105.tsp
python /src/main.py TSPlin318 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/lin318.tsp
python /src/main.py TSPlinhp318 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/linhp318.tsp
python /src/main.py TSPnrw1379 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/nrw1379.tsp
python /src/main.py TSPp654 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/p654.tsp
python /src/main.py TSPpcb442 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/pcb442.tsp
python /src/main.py TSPpcb1173 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/pcb1173.tsp
python /src/main.py TSPpcb3038 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/pcb3038.tsp
python /src/main.py TSPpr136 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/pr136.tsp
python /src/main.py TSPpr144 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/pr144.tsp
python /src/main.py TSPpr152 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/pr152.tsp
python /src/main.py TSPpr226 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/pr226.tsp
python /src/main.py TSPpr264 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/pr264.tsp
python /src/main.py TSPpr299 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/pr299.tsp
python /src/main.py TSPpr439 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/pr439.tsp
python /src/main.py TSPpr1002 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/pr1002.tsp
python /src/main.py TSPpr2392 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/pr2392.tsp
python /src/main.py TSPrat195 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/rat195.tsp
python /src/main.py TSPrat575 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/rat575.tsp
python /src/main.py TSPrd400 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/rd400.tsp
python /src/main.py TSPrl1304 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/rl1304.tsp
python /src/main.py TSPrl1323 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/rl1323.tsp
python /src/main.py TSPrl1889 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/rl1889.tsp
python /src/main.py TSPrl5915 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/rl5915.tsp
python /src/main.py TSPrl5934 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/rl5934.tsp
python /src/main.py TSPrl11849 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/rl11849.tsp
python /src/main.py TSPts225 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/ts225.tsp
python /src/main.py TSPtsp225 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/tsp225.tsp
python /src/main.py TSPu574 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/u574.tsp
python /src/main.py TSPu724 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/u724.tsp
python /src/main.py TSPu1432 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/u1432.tsp
python /src/main.py TSPu2152 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/u2152.tsp
python /src/main.py TSPusa13509 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/usa13509.tsp
python /src/main.py TSPvm1084 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/vm1084.tsp
python /src/main.py TSPvm1748 --test --sys /benchmarks/build/tsp /instances/TSPLIB95/vm1748.tsp
# N_Queens
python /src/main.py N_Queens --test --sys /benchmarks/build/n_queens 14
python /src/main.py N_Queens2 --test --sys /benchmarks/build/n_queens 15
python /src/main.py N_Queens3 --test --sys /benchmarks/build/n_queens 13
# MATRIX_MULT_ST
python /src/main.py MATRIX_MULT_ST1 --test --sys /benchmarks/build/matrix_mult_st 1000
python /src/main.py MATRIX_MULT_ST2 --test --sys /benchmarks/build/matrix_mult_st 1250
python /src/main.py MATRIX_MULT_ST3 --test --sys /benchmarks/build/matrix_mult_st 1500
python /src/main.py MATRIX_MULT_ST4 --test --sys /benchmarks/build/matrix_mult_st 1750
python /src/main.py MATRIX_MULT_ST5 --test --sys /benchmarks/build/matrix_mult_st 2000
python /src/main.py MATRIX_MULT_ST6 --test --sys /benchmarks/build/matrix_mult_st 2250
python /src/main.py MATRIX_MULT_ST7 --test --sys /benchmarks/build/matrix_mult_st 2500
# MATRIX_MULT
# python /src/main.py MATRIX_MULT --test python /benchmarks/MATRIX_MULT/main.py 10000
# python /src/main.py MATRIX_MULT2 --test python /benchmarks/MATRIX_MULT/main.py 15000
# python /src/main.py MATRIX_MULT3 --test python /benchmarks/MATRIX_MULT/main.py 17500
# python /src/main.py MATRIX_MULT4 --test python /benchmarks/MATRIX_MULT/main.py 18000
# python /src/main.py MATRIX_MULT5 --test python /benchmarks/MATRIX_MULT/main.py 12500
