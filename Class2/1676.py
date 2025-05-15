def fac(n):
    if n <= 1: return 1
    else: return n*fac(n-1)

cnt = 0
n = int(input())
res = str(fac(n))

for i in range(len(res)-1,0, -1):
    if res[i] == '0': cnt += 1
    else: break
    
print(cnt)