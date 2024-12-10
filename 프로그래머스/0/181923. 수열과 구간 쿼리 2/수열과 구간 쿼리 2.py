def solution(arr, queries):
    answer = []
    
    for i in range(len(queries)):
        answer.append([])
        for j in range(queries[i][0], queries[i][1]+1):
            if arr[j]>queries[i][2]:
                answer[i].append(arr[j])
    result = []
    for i in range(len(answer)):
        if len(answer[i]) == 0:
            result.append(-1)
        else:
            result.append(min(answer[i]))
    return result