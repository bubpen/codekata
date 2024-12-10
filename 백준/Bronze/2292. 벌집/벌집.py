n = int(input())-1
i = 1
if n == 0:
    cnt = 1
else:
    while n > i*6:
        n -= i*6
        i +=1
    cnt = i+1
print(cnt)
