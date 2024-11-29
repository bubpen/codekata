t = list(map(int,input().split()))
m = int(input())
t[1] += m
if t[1]>=60:
    t[0] = t[0] + t[1] // 60
    t[1]= t[1] - t[1]//60 * 60
if t[0]>=24:
    t[0] -=24
print(t[0],t[1])