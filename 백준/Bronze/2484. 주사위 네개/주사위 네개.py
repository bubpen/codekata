N = int(input())
result = []
for i in range(N):
    l = list(map(int,input().split()))
    s = set(l)
    if len(s) == 1:
        result.append(50000 + l[0] * 5000)
    elif len(s) == 2:
        count = l.count(max(l))
        if count == 3:
            result.append(10000 + max(l) * 1000)
        elif count == 1:
            result.append(10000 + min(l) * 1000)
        else:
            if l.count(min(l)) == 2:
                result.append(2000 + (max(l) + min(l)) * 500)
    elif len(s) == 3:
        for i in s:
            if l.count(i)==2:
                result.append(1000 + i * 100)
                break
    else:
        result.append(max(l) * 100)
print(max(result))