import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
code={}
n = int(input())
for i in range(n):
    b, c = input().split()
    c = int(c)
    code[b]=c
s = input()
print(code, file=sys.stderr)
print(s, file=sys.stderr)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

if len(code)==0:
    print('DECODE FAIL AT INDEX 0')
    quit()

max_key=max(map(len,code))
result= ''
buffer=''
i=0
breaked=False
while i < len(s):
    buffer+=s[i]
    if len(buffer)<=max_key:
        if buffer in code:
            print(buffer+' in code', file=sys.stderr)
            result+=chr(code[buffer])
            buffer=''
    else:
        print(buffer, file=sys.stderr)
        result='DECODE FAIL AT INDEX 0'
        breaked=True
        break
    i+=1

if not breaked:

    if buffer not in code and len(buffer)>0:
        result='DECODE FAIL AT INDEX '+str(len(s)-len(buffer))

print(result)