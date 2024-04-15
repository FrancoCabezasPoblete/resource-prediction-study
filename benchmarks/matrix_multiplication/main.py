from icecream import ic
import numpy as np
import sys
import time

if len(sys.argv) < 2:
    ic("Usage: python main.py <n:int>")
    sys.exit(1)
n = int(float(sys.argv[1]))
start_time = time.time()
a = np.random.rand(n, n)
b = np.random.rand(n, n)
c = a@b
ic(f"Time taken for {n}-dim: {time.time() - start_time}[s]")