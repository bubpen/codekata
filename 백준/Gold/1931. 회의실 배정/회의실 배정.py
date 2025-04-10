n = int(input())
meetings = []
for _ in range(n):
    s, e = map(int, input().split())
    meetings.append((s, e))
meetings.sort(key = lambda x: (x[1], x[0]))

count = 0
finish = 0
today = []
for start, end in meetings:
    if start >= finish:
        today.append((start, end))
        finish = end
print(len(today))