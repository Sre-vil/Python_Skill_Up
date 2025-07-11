import sys
input = sys.stdin.readline

test_case = int(input())
res_list = []

for _ in range(test_case):
    contents, target_index = map(int, input().split())
    priority_list = list(map(int, input().split()))
    target_priority = priority_list[target_index]
    max_index = priority_list.index(max(priority_list))
    
    # target_index의 중요도가 중복x 인 경우
    if priority_list.count(target_priority) == 1:
        rank = sorted(priority_list, reverse=True)
        res = rank.index(priority_list[target_index]) + 1
    # target_index의 중요도가 중복o 인 경우 
    else:
        count = 0
        while target_priority != max(priority_list):
            count += 1
            max_index = priority_list.index(max(priority_list))
            priority_list.pop(max_index)
        if target_index > max_index:
            # 1 1 9 1 1 1
            # 1 1 1 1 1
            # target이 5번이었다면
            # 5 - 2 = 3
            # target이 4번이었다면
            # 4 - 2 = 2
            res = count + target_index - max_index
        else:
            # target이 0번이었다면
            # len(target[max_index:]) + 1 + count
            res = count + len(priority_list[max_index:]) + target_index + 1
    res_list.append(res)

print(*res_list, sep="\n")