def solution(arr, queries):
    answer = arr[:]
    for i in queries:
        for n in range(i[0],i[1]+1):
            if n % i[2] == 0:
                answer[n] = answer[n] + 1
            else:
                answer[n] = answer[n]
    return answer