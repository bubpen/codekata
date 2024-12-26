def solution(arr, k):
    answer = []
    i = 0
    while len(answer) < k:
        if i < len(arr):
            if arr[i] not in answer:
                answer.append(arr[i])
        else:
             answer.append(-1)
        i += 1
    return answer