N, K = map(int,input().split())
num = []
if N == 0:
    print(0)
else:
    for i in range(1,N+1):
        if N % i == 0:
            num.append(i)
    if len(num) < K:
        print(0)
    else:
        print(num[K-1])