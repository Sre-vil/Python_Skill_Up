# 최대공약수 및 최소공배수  
def gcd(a, b):
    if b == 0: return a
    return gcd(b, a%b)

def lcm(a, b):
    return a * b // gcd(a, b)

a, b = map(int, input().split())
print(gcd(a, b))
print(lcm(a, b))