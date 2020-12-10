import sys
import math
import numpy as np

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
x=[]
n = int(input())
for i in range(n):
    pi = int(input())
    x.append(pi)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
x = sorted(x)
print(np.diff(x), file=sys.stderr)
print(abs(min(np.diff(x))))
