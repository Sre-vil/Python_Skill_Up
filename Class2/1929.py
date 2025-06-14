import sys
input = sys.stdin.readline

m, n = map(int, input().split())

is_prime = [True] * (n+1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(n**0.5)+1):
    if is_prime[i]:
        for j in range(i*i, n+1, i): is_prime[j] = False

primes = []
for i in range(m, n+1):
    if is_prime[i]: primes.append(i)

for i in primes: print(i)
