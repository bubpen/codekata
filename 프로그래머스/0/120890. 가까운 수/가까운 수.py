def solution(array, n):
    answer = []
    for i in array:
        answer.append(abs(n-i))
    result = []
    for i in array:
        if abs(n-i)==min(answer):
            result.append(i)
    if len(result) >1:
        return min(result)
    else:
        return result[0]