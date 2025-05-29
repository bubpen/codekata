from collections import deque
import sys
input = lambda: sys.stdin.readline().strip()
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [-1] * (n + 1)
distance[x] = 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
for i in range(1, n + 1):
    graph[i].sort()
queue = deque([x])
while queue:
    current = queue.popleft()
    for neighbor in graph[current]:
        if distance[neighbor] == -1:
            distance[neighbor] = distance[current] + 1
            queue.append(neighbor)
result = []
for i in range(1, n + 1):
    if distance[i] == k:
        result.append(i)
if result:
    for city in result:
        print(city)
else:
    print(-1)