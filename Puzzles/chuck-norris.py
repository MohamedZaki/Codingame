import sys
import math
from itertools import groupby
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def splitter(text):
    return [''.join(group) for key, group in groupby(text)]

message = input()
result = ''
binary = ''
for char in message:
    b=bin(ord(char))[2:]
    binary += '0'*(7-len(b))+b 

print(binary, file=sys.stderr)
groups = splitter(binary)
print(groups, file=sys.stderr)
for idx,group in enumerate(groups):
    if idx>0:
        result+=' '
    if group[0]=='1':
        result+='0 '
        result+='0'*len(group)
    else:
        result+='00 '
        result+='0'*len(group)

print(result)
