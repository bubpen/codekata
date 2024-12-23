def solution(n):
    answer = list(str(n).strip())
    answer = sorted(answer,reverse = True)
    answer = int(''.join(answer))
    return answer