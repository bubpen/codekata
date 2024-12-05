n = int(input())
cnt = int(n)
for i in range(n):
    string = input()
    for j in range(len(string)-1):
        if string[j] == string[j+1]:
            continue
        elif string[j] in string[j+1:]:
            cnt -= 1
            break
print(cnt)