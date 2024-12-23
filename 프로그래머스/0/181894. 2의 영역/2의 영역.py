def solution(arr):
    answer = []
    if 2 in arr:
        idx = []
        for i in range(len(arr)):
            if arr[i] == 2:
                idx.append(i)
        if len(idx) == 1:
            answer = [2]
        else:
            answer = arr[idx[0]: idx[-1]+1]
    else:
        answer.append(-1)
    return answer