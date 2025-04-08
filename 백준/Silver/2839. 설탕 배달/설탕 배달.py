n = int(input())
first = n
second = n
count = 0
while first >= 3:
    if first >= 5:
        first -= 5
        count += 1
    else:
        first -= 3
        count += 19
if first != 0:
    count = -1
result = [count]
count = 0
while second >= 3:
    second -= 3
    count += 1
    if second % 5 == 0:
        count += second // 5
        second -= second // 5 * 5
if second != 0:
    count = -1
result.append(count)
for i in range(result.count(-1)):
    result.remove(-1)
if result:
    print(min(result))
else:
    print(-1)