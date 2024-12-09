def solution(n):
    answer = 0
    string = str(n)
    for num in string:
        answer += int(num)
    return answer