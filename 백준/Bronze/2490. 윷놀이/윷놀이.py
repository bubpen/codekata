for i in range(3):
    l = list(map(int,input().split()))
    if l.count(0) == 1:
        print('A')
    elif l.count(0) == 2:
        print('B')
    elif l.count(0) == 3:
        print('C')
    elif l.count(0) == 4:
        print('D')
    elif l.count(1) == 4:
        print('E')
