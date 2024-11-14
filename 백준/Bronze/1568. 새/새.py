N=int(input())
b = 1
t = 0
while N > 0:
    N -=b
    t += 1
    if N == 0:
        break
    elif b >= N:
        b = 1
    else:
        b += 1

print(t)