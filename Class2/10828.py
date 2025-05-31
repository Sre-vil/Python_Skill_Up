import sys
input = sys.stdin.readline

n = int(input())
res = []

for _ in range(n):
    cmd = input().strip().split()

    if cmd[0] == 'push':
        res.append(cmd[1])
    elif cmd[0] == 'pop':
        print(res.pop() if res else -1)
    elif cmd[0] == 'size':
        print(len(res))
    elif cmd[0] == 'empty':
        print(0 if res else 1)
    elif cmd[0] == 'top':
        print(res[-1] if res else -1)