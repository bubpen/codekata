def solution(brown, yellow):
    answer = []
    for y in range(3, brown//2):
        for x in range(3, brown//2):
            if 2*x + 2*y - 4 == brown and (x-2)*(y-2) == yellow and x >= y:
                answer = [x, y]
                break
        if answer != []:
            break
    return answer