n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]
meetings.sort(key = lambda x: (x[1], x[0]))

count = 0
finish = 0
for start, end in meetings:
    if start >= finish:
        count += 1
        finish = end
print(count)