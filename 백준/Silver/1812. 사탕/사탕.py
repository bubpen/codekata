n = int(input())
s = []
for i in range(n):
    s.append(int(input()))
a = [0] * n
a[0] = s[0]
for i in range(1, n):
    if i % 2 == 0:
        a[0] += s[i]
    else:
        a[0] -= s[i]
a[0] = a[0] // 2
for i in range(1, n):
    a[i] = s[i-1] - a[i-1]
for num in a:
    print(num)