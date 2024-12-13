while True:
    side_list = []
    side = list(map(int,input().split()))
    side.sort()
    if side.count(0) == 3:
        break
    elif side[2] >= side[0] + side[1]:
        print('Invalid')
    elif side.count(side[0]) == 3:
        print('Equilateral')
    elif side.count(side[0]) ==2 or side.count(side[1]) == 2:
        print('Isosceles')
    else:
        print('Scalene')