import sys
input = sys.stdin.readline

n = int(input())
alist = set(map(int, input().split()))

m = int(input())
blist = list(map(int, input().split()))

for i in blist:
    if i in alist: print(1)
    else: print(0)