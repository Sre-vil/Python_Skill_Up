import sys
input = sys.stdin.readline

n = int(input())
res = []

for _ in range(n):
    tmp = input()
    stack = []
    for i in tmp:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break
    if len(stack) == 0: res.append('YES')
    else: res.append('NO')

for i in res:
    print(i)