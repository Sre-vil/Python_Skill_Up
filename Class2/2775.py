# 깊은 복사와 얕은 복사 이슈 
test_case = int(input())

output = []
for _ in range(test_case):
    k = int(input())
    n = int(input())
    tmp = []
    res = []
    for a in range(k+1):
        for b in range(n):
            if a==0: 
                tmp.append(b+1)
                res.append(b+1)
            else:
                res[b] = sum(tmp[:b+1])
        tmp = res.copy() 
    output.append(res[n-1])

for i in output:
    print(i)