import sys
input = sys.stdin.readline

n = int(input())
current_num = 1
result = []
stack = []
is_possible = True

for _ in range(n):
    tmp = int(input())
    
    while current_num <= tmp:
        stack.append(current_num)
        result.append('+')
        current_num += 1
    
    if tmp == stack[-1]:
        stack.pop()
        result.append('-')
    else:
        is_possible = False
        break

if is_possible:
    for i in result: print(i)
else: print("NO")