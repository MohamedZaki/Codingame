print(min(sorted(map(int,input().split()))[::-1],key=abs)if int(input())else 0)