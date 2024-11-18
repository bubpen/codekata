def solution(numbers, direction):
    answer = []
    for i in numbers:
        answer.append(i)
    if direction == 'right':
        for i in range(len(numbers)):
            answer[i] = numbers[i-1]
    elif direction == 'left':
        for i in range(len(numbers)):
            if i+1 == len(numbers):
                answer[i] = numbers[0]
            else:
                answer[i] = numbers[i+1]
    return answer