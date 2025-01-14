def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        arr1[i] = format(arr1[i], 'b')
        if len(arr1[i])<n:
            arr1[i] = '0' * (n-len(arr1[i])) + arr1[i]
        arr2[i] = format(arr2[i], 'b')
        if len(arr2[i])<n:
            arr2[i] = '0' * (n-len(arr2[i])) + arr2[i]
        position = ''
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                position = position + '#'
            else:
                position = position + ' '
        answer.append(position)
    return answer