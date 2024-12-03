N, M = map(int, input().split())
b = []
for i in range(N):
    b.append(str(i+1))
for i in range(M):
    x,y = map(int,input().split())
    b[x-1:y] = reversed(b[x-1:y])
print(' '.join(b))