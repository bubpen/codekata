e,f,c = map(int,input().split())
a = e+f
b = 0
while a >= c:
    d = a//c
    b = b+ d
    a =  a-c*d +d
print(b)