res = []

while True:
    tmp = input()
    if tmp=='.': break
    
    if tmp.count('(') == tmp.count(')') and tmp.count('[') == tmp.count(']'):
        res.append('yes')
    else: res.append('no')

print(*res)