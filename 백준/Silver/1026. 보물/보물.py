n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = 0
B = b.copy()
B.sort(reverse = True)
a.sort()
for j,k in zip(a, B):
    result += j*k
print(result)
