for i in range(3):
    tmp = input()
    if tmp != "FizzBuzz" and tmp!="Fizz" and tmp!="Buzz":
        res = int(tmp)
        cnt = i
    else: continue

if cnt==0: res += 3
elif cnt==1: res += 2
elif cnt==2: res +=1

if res%3!=0 and res%5!=0: print(res)
elif res%3==0 and res%5!=0: print("Fizz")
elif res%3!=0 and res%5==0: print("Buzz")
else: print("FizzBuzz")