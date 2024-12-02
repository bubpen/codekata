a,b = map(int,input().split())
nl = list(map(int,input().split()))
ln = []
for i in range(a):
    if nl[i] < b:
        ln.append(str(nl[i]))
print(' '.join(ln))