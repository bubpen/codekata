s = int(input())
n = 2*s
for i in range(1, int(n**(1/2))+2):
    if n-i == i**2:
        print(i)
        break
    elif n-i < i**2:
        print(i-1)
        break