n = int(input())
for i in range(n):
    a,b,c = map(int,input().split())
    x,y =1,0
    for num in range(c):
        y += 1
        if y == a+1:
            x += 1
            y = 1
    if x > 9:
        print(int(str(y) + str(x)))
    else:
        print(int(str(y) + '0' + str(x)))