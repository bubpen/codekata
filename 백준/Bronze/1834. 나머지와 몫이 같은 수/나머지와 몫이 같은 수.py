N = int(input())
i = 1
n = []
while i // N < N:
    if i//N == i%N:
        n.append(i)
        i +=N
    else:
        i += 1

result = 0
for i in range(len(n)):
    result += n[i]
print(result)