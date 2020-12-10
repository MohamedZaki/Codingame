from itertools import combinations

w, h, count_x, count_y = [int(i) for i in input().split()]

w_points = [0,w]
h_points = [0,h]
for i in input().split():
    w_points.append(int(i))

for i in input().split():
    h_points.append(int(i))


widths = sorted(list(map(lambda xy: abs(xy[0]-xy[1]), combinations(w_points,2))))
heights = sorted(list(map(lambda xy: abs(xy[0]-xy[1]), combinations(h_points,2))))

c=0
for x in widths:
    c += heights.count(x)
print(c)