n = int(input())
c = list(map(int,input().split()))
u = []
for i in range(1,len(c)):
    u.append(c[i]-c[i-1])
s = 0
i = 0
a = 0
s = 0
while i <len(u):
    if u[i]>0:
        a +=u[i]
    else:
        if s<a:
            s = a
        a =0
    if i == len(u)-1:
        if s<a:
            s =a
    i +=1
print(s)