def solution(food):
    answer = ''
    for i in range(1,len(food)):
        for r in range(food[i]//2):
            answer = answer + str(i)
    return answer + '0' + answer[::-1]