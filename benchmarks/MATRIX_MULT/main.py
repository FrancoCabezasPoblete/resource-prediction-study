import numpy as np
import sys

if len(sys.argv) < 2:
    print("Usage: python main.py <n:int>")
    sys.exit(1)
n = int(float(sys.argv[1]))
a = np.random.rand(n, n)
b = np.random.rand(n, n)
c = a@b