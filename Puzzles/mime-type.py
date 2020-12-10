import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
types = {}
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    types[ext.lower()] = mt
    #print(ext, mt)
for i in range(q):
    fname = input()  # One file name per line.
    if '.' in fname:
        fext = fname.split('.')[-1].lower()
    else:
        fext = ''
    if fext in types.keys():
        print('DEBUG', fname,types[fext], file=sys.stderr)
        print(types[fext])
    else:
        print('DEBUG', fname, file=sys.stderr)
        print('UNKNOWN')
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
#print("UNKNOWN")
