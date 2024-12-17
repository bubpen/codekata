n = int(input())
answer  = 0
for i in range(n):
    s = str(i)
    a = 0
    for j in str(i):
        a += int(j)
    if a + i == n:
        answer = i
        break
print(answer)