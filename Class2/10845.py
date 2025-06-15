import sys
input = sys.stdin.readline

n = int(input())
res = []

for _ in range(n):
    cmd = input().strip().split()
    
    if cmd[0] == 'push':
        res.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(res) != 0: print(res.pop(0))
        else: print(-1)
    elif cmd[0] == 'size':
        print(len(res))
    elif cmd[0] == 'empty':
        if len(res) != 0: print(0)
        else: print(1)
    elif cmd[0] == 'front':
        if len(res) != 0: print(res[0])
        else: print(-1)
    elif cmd[0] == 'back':
        if len(res) != 0: print(res[-1])
        else: print(-1)