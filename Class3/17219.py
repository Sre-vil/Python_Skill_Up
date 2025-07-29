import sys
input = sys.stdin.readline

n, m = map(int, input().split())

link_and_pw = {}
output = []

for _ in range(n):
    link, pw = input().split()
    link_and_pw[link] = pw

for _ in range(m):
    target = input().strip()
    output.append(link_and_pw[target])

for i in output:
    print(i)