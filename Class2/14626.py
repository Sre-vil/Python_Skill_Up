n = input()

sum = 0

for i in range(len(n)-1):
    if n[i] == '*': 
        tmp = i
        continue
    elif i%2 == 0: sum += int(n[i])
    else: sum += int(n[i])*3

for i in range(10):
    if tmp%2 == 0 and (sum+i+int(n[-1]))%10 == 0:
        print(i)
    elif tmp%2 != 0 and (sum+i*3+int(n[-1]))%10 == 0:
        print(i)