N = int(input())
result = []
for i in range(N):
    l = list(map(int,input().split()))
    if l.count(l[0])==3:
        result.append(10000+l[0]*1000)
    elif l.count(l[0])==2:
        result.append(1000+l[0]*100)
    elif l.count(l[1]) == 2:
        result.append(1000+l[1]*100)
    else:
        result.append(max(l)*100)
print(max(result))