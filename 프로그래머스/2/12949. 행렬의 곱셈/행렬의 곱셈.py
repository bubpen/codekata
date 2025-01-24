def solution(arr1, arr2):
    answer = []
    M = len(arr1)
    N = len(arr1[0])
    L = len(arr2[0])
    for m in range(M):
        answer.append([])
        for l in range(L):
            result = 0
            for n in range(N):
                result += arr1[m][n]*arr2[n][l]
            answer[m].append(result)
    return answer