for i in range(3):
    n = int(input())
    result = 0
    for j in range(n):
        a = int(input())
        result += a
    if result == 0:
        print(0)
    elif result > 0:
        print("+")
    else:
        print('-')