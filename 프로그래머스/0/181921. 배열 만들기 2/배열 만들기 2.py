def solution(l, r):
    answer = [i for i in range(l, r+1) if all(w in '05' for w in str(i))]
    return answer if answer else [-1]