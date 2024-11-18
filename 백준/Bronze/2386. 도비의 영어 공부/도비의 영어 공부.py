while True:
    a = list(map(str,input().split(' ')))
    if a[0] == '#':
        break
    count = 0
    for i in range(1,len(a)):
        for j in range(len(a[i])):
            if a[i][j].lower() == a[0]:
                count+=1
    print(f'{a[0]} {count}')