a,b = map(int,input().split())
if a>b:
    a,b = b,a
s = ((b - a + 1) * (a+b))//2
print(s)