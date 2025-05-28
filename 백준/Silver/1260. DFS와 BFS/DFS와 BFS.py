from collections import deque
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
for i in range(1, n+1):
    graph[i].sort()
visited = [False] * (n + 1)
stack = [v]
dfs_result = []
while stack:
    node = stack.pop()
    if not visited[node]:
        visited[node] = True
        dfs_result.append(node)
        for neighbor in reversed(graph[node]):
            if not visited[neighbor]:
                stack.append(neighbor)
bfs_result = []
visited = [False] * (n + 1)
queue = deque([v])
visited[v] = True
while queue:
    node = queue.popleft()
    bfs_result.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            queue.append(neighbor)
print(' '.join(map(str, dfs_result)))
print(' '.join(map(str, bfs_result)))