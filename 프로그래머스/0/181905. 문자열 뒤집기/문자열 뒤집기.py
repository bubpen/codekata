def solution(my_string, s, e):
    answer = list(my_string)
    arr = []
    for i in range(s,e+1):
        arr.insert(0,answer[i])
    for i in range(len(arr)):
        answer[i+s] = arr[i]
    return ''.join(answer)