import sys
input = sys.stdin.readline

def my_round(val):
    return int(val + 0.5)

n = int(input())

if n == 0: print(0)
else:
    tmp = sorted([int(input()) for _ in range(n)])
    ex = my_round(n*0.15)
    
    if ex > 0: res = tmp[ex:-ex]
    else: res = tmp

    
    if res:
        avg = my_round(sum(res)/len(res))
        print(avg)
    else: print(0)