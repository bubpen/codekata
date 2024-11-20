l = list(map(int,input().split()))
s = 0
for i in l:
    s = s + i**2
l.append(s%10)
print(l[-1])