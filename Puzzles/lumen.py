import sys
import math
import numpy as np

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
l = int(input())
room=[]
for i in range(n):
    for cell in input().split():
        room.append(cell)

room = np.array(room).reshape((n,n))
room = np.where(room=='X', 0, room)
room = np.where(room=='C', l, room)
room=room.astype(int)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
#print(room)
rows, cols = np.where(room>0)

for x in range(l,1,-1):
    for i in range(n):
        for j in range(n):
            if room[i,j]==x:
                if (i-1>=0)and(j-1>=0):
                    room[i-1,j-1]=max(x-1,room[i-1,j-1])
                if ((i+1>=0)and(j+1>=0))and(i+1<n and j+1<n):
                    room[i+1,j+1]=max(x-1,room[i+1,j+1])
                if ((i-1>=0)and(j+1>=0))and(i-1>=0 and j+1<n):
                    room[i-1,j+1]=max(x-1,room[i-1,j+1])
                if ((i+1>=0)and(j-1>=0))and(i+1<n and j-1>=0):
                    room[i+1,j-1]=max(x-1,room[i+1,j-1])
                if i-1>=0:
                    room[i-1,j]=max(x-1,room[i-1,j])
                if i+1<n:
                    room[i+1,j]=max(x-1, room[i+1,j])
                if j-1>=0:
                    room[i,j-1]=max(x-1, room[i,j-1])
                if j+1<n:
                    room[i,j+1]=max(x-1, room[i,j+1])

print(np.count_nonzero(room==0))
