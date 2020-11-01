import sys

abc='ABCDEFGHIJKLMNOPQRSTUVWXYZ?'
l = int(input())
h = int(input())
t = input().upper()

print(l,h,t, file=sys.stderr)

ltr=[]
for i in range(h):
    row = input()
    ltr.append(row)

for line in range(h):
    r=''
    for x in t:
        if x not in abc:
            x='?'
        idx = abc.index(x)
        r+=ltr[line][idx*l:idx*l+l]
    print(r)