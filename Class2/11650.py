import sys
input = sys.stdin.readline

n = int(input())
res = []

for _ in range(n):
    x, y = map(int, input().split())
    res.append((x,y))
    
res.sort()

for i in res:
    print(*i)