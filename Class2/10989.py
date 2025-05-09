import sys
input = sys.stdin.readline

n = int(input())
res = [0] * 10000
for _ in range(n):
    tmp = int(input())
    res[tmp-1] += 1

for i, v in enumerate(res):
    if v != 0:
        for _ in range(v): print(i+1)
    else:
        continue
    