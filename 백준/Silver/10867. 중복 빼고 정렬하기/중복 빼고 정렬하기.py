n = int(input())
array = list(map(int, input().split()))
answer = list(set(array))
answer.sort()
for i in range(len(answer)):
    if i < len(answer)-1:
        print(answer[i], end = ' ')
    else:
        print(answer[i])