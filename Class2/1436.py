n = int(input())
tmp = 666
cnt = 0

while True:
    if '666' in str(tmp):
        cnt += 1
    if cnt == n: break
    
    tmp += 1

print(tmp)