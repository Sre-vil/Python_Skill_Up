# A : 낮에 올라가는 높이(미터)
# B : 밤에 미끄러지는 높이(미터)
# V : 나무의 높이(미터)  

a, b, v = map(int, input().split())

# 모두 올라가는데 걸리는 일수를 n
# n일 동안 a만큼 올라감
# n일 동안 b만큼 내려감 
# an - b(n-1) = v
# an - bn + b = v
# (a-b)n = v-b
# n = (v-b)/(a-b)

day = int((v-b)/(a-b))
if (v-b) % (a-b): day += 1
print(day)