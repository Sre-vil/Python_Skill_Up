import sys
import time
import os
import psutil

process = psutil.Process(os.getpid())
memory_info = process.memory_info()

start_time = time.time()
input = sys.stdin.readline

n = int(input())
person = []
cnt = [1]*n

for _ in range(n):
    x, y = map(int, input().split())
    person.append((x,y))

# 모두가 1등에서 시작
# 자기보다 덩치가 큰 사람이 있으면 등수가 내려가는 구조
idx = 0
while idx < n:
    for i in range(n):
        if i == idx: continue
        if person[idx][0] < person[i][0] and person[idx][1] < person[i][1]:
            cnt[idx] += 1
    idx += 1
    
print(*cnt)
end_time = time.time()

print(f"실행 시간 : {end_time - start_time:.4f}초")
print(f"사용 메모리 : {memory_info.rss/(1024*1024):.2f}MB")