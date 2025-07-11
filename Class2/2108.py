import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    tmp = int(input())
    arr.append(tmp)
    
# 산술평균
avg = round(sum(arr)/len(arr))

# 중앙값
arr.sort()
mid_idx = (n-1)//2
mid = arr[mid_idx]

# 최빈값 
counts = {}
arr_set = set(arr)
for i in arr_set:
    counts[i] = arr.count(i)

max_value = max(counts.values())
multi_list = []

for k,v in counts.items():
    if max_value == v: multi_list.append(k)

multi_list.sort()
if len(multi_list) > 1: max_value = multi_list[1]
else: max_value = multi_list[0]

# 범위 
diff = max(arr) - min(arr)

print(avg)
print(mid)
print(max_value)
print(diff)