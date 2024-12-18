def solution(numbers):
    a = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                continue
            else:
                a.append(numbers[i] * numbers[j])
    
    return max(a)