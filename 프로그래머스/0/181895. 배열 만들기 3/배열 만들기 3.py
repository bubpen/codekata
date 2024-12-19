def solution(arr, intervals):
    answer = []
    for i in intervals:
        a = arr[i[0]:i[1]+1]
        for n in a:
            answer.append(n)
    return answer