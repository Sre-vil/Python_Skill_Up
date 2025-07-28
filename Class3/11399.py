import sys
input = sys.stdin.readline

n = int(input())
personal_time_list = list(map(int, input().split()))

personal_time_list.sort()

tmp_time = 0
total_time_list = []

for i in personal_time_list:
    tmp_time += i
    total_time_list.append(tmp_time)
    
min_time = sum(total_time_list)
print(min_time)