n, k = map(int, input().split())

li = [i for i in range(1, n+1)]
res = []
idx = 0

# 1 2 3 4 5 6 7 | target_idx = 2(3)
# 1 2 4 5 6 7 | target_idx = 4(6)
# 1 2 4 5 7 | target_idx = 6 -> 6-5=1 => target_idx=1(2)
# 1 4 5 7 | target_idx=3(7)
# 1 4 5 | target_idx=5 -> 5-3=2 => target_idx=2(5)
# 1 4 | target_idx=4 -> 4-2=2 -> 2-2=0 => target_idx=0(4)

for i in range(n):
    idx += k-1
    while idx > len(li)-1: idx -= len(li)
    else:
        res.append(li[idx])
        li.remove(li[idx])

res_str = ', '.join(map(str, res))
print(f"<{res_str}>")