def solution(num_str):
    answer = 0
    for i in num_str:
        if i in '1234567890':
            answer += int(i)
    return answer