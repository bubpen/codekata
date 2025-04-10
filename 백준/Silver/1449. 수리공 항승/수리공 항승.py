n, l = map(int, input().split())
location = list(map(int, input().split()))
location.sort()
answer = 1
tape = l -1
for i in range(1,n):
    if location[i] - location[i-1] <= tape:
        tape -= (location[i] - location[i-1])
    else:
        answer += 1
        tape = l - 1
print(answer)