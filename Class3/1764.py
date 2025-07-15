import sys
input = sys.stdin.readline

n, m = map(int, input().split())

no_listen = set()
no_see = set()

for _ in range(n):
    tmp = input().strip()
    no_listen.add(tmp)

for _ in range(m):
    tmp = input().strip()
    no_see.add(tmp)

dup = list(no_listen & no_see)
dup.sort()

print(len(dup))
for i in dup: print(i)