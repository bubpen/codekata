def solution(numbers):
    answer = 0
    for n in '1234567890':
        if int(n) not in numbers:
            answer += int(n)
    return answer