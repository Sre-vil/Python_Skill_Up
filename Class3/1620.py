import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}

for i in range(1, n+1):
    name = input().strip()
    dic[i] = name

number_dic = {v:k for k,v in dic.items()}

for _ in range(m):
    tmp = input().strip()
    if tmp.isdigit():
        print(dic[int(tmp)])
    else:
        print(number_dic.get(tmp))