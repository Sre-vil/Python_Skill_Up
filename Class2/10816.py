import sys 
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
basis = list(map(int, input().split()))

# 검색 대상 : cards 
# target : basis 
# 이 경우는 검색 대상에 중복 값이 존재한다는 문제  

# 검색 대상 : basis
# target : cards
# 이 경우는 basis 순서가 꼬인다는 문제 

count = {}

# cards 원소를 key로 하고, 개수를 value로 가지는 딕셔너리 생성 
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

for key in basis:
    if key in count:
        print(f"{count[key]}", end=' ')
    else:
        print(0, end=' ')