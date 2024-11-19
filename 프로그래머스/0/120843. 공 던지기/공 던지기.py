def solution(numbers, k):
    n = 0
    i = 0
    while n < (k-1):
        i += 2
        if i >=len(numbers):
            i = i - len(numbers)
        n += 1
    answer = numbers[i]
    return answer