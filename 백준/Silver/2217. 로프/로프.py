n = int(input())
rope = []
for i in range(n):
    rope.append(int(input()))
rope.sort()
count = len(rope)
weights = []
for i in rope:
    weights.append(i * count)
    count -= 1
answer = max(weights)
print(answer)