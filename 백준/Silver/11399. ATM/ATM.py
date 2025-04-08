n = int(input())
time = list(map(int, input().split()))
time.sort()
answer = 0
last = 0
for i in time:
    if last:
        i += last
        answer += i
        last = i
    else:
        answer += i
        last = i
print(answer) 