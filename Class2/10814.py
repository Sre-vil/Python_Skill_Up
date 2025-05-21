import sys
input = sys.stdin.readline

n = int(input())
tmp = {}

for i in range(n):
    age, name = input().split()
    tmp[(int(age), i)] = name

tmp = sorted(tmp.items())

for i in range(n):
    print(tmp[i][0][0], tmp[i][1])