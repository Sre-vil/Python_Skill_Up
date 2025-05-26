while True:
    tmp = input()
    res = []
    
    if tmp == '.': break
    
    for i in tmp:
        if i == '(' or i == '[':
            res.append(i)
        elif i == ']':
            if len(res) != 0 and res[-1] == '[':
                res.pop()
            else:
                res.append(i)
                break
        elif i == ')':
            if len(res) != 0 and res[-1] == '(':
                res.pop()
            else:
                res.append(i)
                break
    
    if len(res) == 0: print("yes")
    else: print("no")