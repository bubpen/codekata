def solution(my_string, queries):
    answer = list(my_string)
    for i in queries:
        a = []
        for n in range(i[0], i[1]+1):
            a.insert(0,answer[n])
        for idx in range(len(a)):
            answer[idx + i[0]] = a[idx]
    return ''.join(answer)