def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        answer.append([])
        for idx in range(len(arr1[i])):
            answer[i].append(arr1[i][idx] + arr2[i][idx])
    return answer