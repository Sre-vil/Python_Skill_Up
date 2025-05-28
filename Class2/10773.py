import sys
input = sys.stdin.readline

k = int(input())
res = []

for i in range(k):
    tmp = int(input())
    
    if tmp == 0:
        res.pop()
    else:
        res.append(tmp)

print(sum(res))