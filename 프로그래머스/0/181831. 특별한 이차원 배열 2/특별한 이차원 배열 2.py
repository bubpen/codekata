def solution(arr):
    answer = 1
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if i == j:
                pass
            else:
                if arr[i][j] != arr[j][i]:
                    answer = 0
                    break
        if answer == 0:
            break
    return answer