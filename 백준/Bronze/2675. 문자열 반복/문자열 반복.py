N = int(input())
for i in range(N):
    n, string = input().split()
    a = ''
    for j in range(len(string)):
        a = a + int(n)*string[j]
    print(a)