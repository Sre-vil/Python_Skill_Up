def fac(n):
    if n<=1: return 1
    else: return n*fac(n-1)

n, k = map(int, input().split())
res = fac(n)/(fac(n-k)*fac(k))
print(int(res))