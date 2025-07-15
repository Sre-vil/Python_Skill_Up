import sys
input = sys.stdin.readline

n = int(input())
s = set()
res = []

for _ in range(n):
    tmp = input()
    if 'all' in tmp:
        s = {i for i in range(1, 21)}
        continue
    elif 'empty' in tmp:
        s = set()
        continue
    else:
        cmd, param = tmp.split()
        param = int(param)
        if cmd == 'add':
            s.add(param)
        elif cmd == 'remove':
            s.discard(param)
        elif cmd == 'check':
            if param in s: 
                print(1)
            else: 
                print(0)
        elif cmd == 'toggle':
            if param in s:
                s.remove(param)
            else:
                s.add(param)
