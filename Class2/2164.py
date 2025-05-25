import sys
input = sys.stdin.readline

n = int(input())
res = list(range(1, n+1))

# [1,2,3,4] -> [2,3,4] -> [3,4,2]
# [3,4,2] -> [2,4]
# [2,4] -> [4]

# while len(res) > 1:
#     res.pop(0)
#     tmp = res[0]
#     res[:-1] = res[1:]
#     res[-1] = tmp

# print(*res)

point = 0
while point < len(res)-1:
    point += 1
    res.append(res[point])
    point += 1

print(res[point])