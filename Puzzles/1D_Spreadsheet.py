import sys

def decode(cell, idx):
    if result[idx] != None:
        return result[idx]
    op = cell[0]
    a = cell[1]
    b = cell[2]
    if '$' in a:
        aval = decode(data[int(a[1:])], int(a[1:]))
    else:
        aval = int(a)
    if '$' in b:
        bval = decode(data[int(b[1:])], int(b[1:]))
    elif '_' in b:
        bval = 0
    else:
        bval = int(b)

    if op == 'VALUE':
        result[idx] = aval
        return aval
    elif op == 'ADD':
        result[idx] = aval+bval
        return aval+bval
    elif op == 'SUB':
        result[idx] = aval-bval
        return aval-bval
    elif op == 'MULT':
        result[idx] = aval*bval
        return aval*bval


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
debug = 1
n = int(input())

data = []
result = [None]*n
for i in range(n):
    operation, arg_1, arg_2 = input().split()
    data.append([operation, arg_1, arg_2])

if debug:
    print(data, file=sys.stderr)
    print(result, file=sys.stderr)

#Decode all 
for idx,cell in enumerate(data):
    result[idx] = decode(cell,idx)

for i in range(n):
    print(result[i])
