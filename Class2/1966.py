import sys
input = sys.stdin.readline

test_case = int(input())
res = []

for _ in range(test_case):
    # contents: 문서의 개수, target_index: 찾고자 하는 문서의 위치 
    contents, target_index = map(int, input().split())
    # priority_list: 중요도 리스트
    priority_list = list(map(int, input().split()))
    
    # (중요도, 초기 인덱스)를 저장
    queue = [(p, i) for i, p in enumerate(priority_list)]
    # count: 몇 번재로 인쇄되었는지 기록할 변수
    count = 0
    
    while queue:
        current_doc = queue.pop(0)
        
        if any(current_doc[0] < other_doc[0] for other_doc in queue):
            queue.append(current_doc)
        else:
            count += 1
            if current_doc[1] == target_index:
                res.append(count)
                break
            
print(*res, sep='\n')