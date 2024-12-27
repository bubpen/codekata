def solution(strArr):
    length = []
    for i in strArr:
        length.append(len(i))
    i =1
    answer = 0
    while i in length:
        if answer < length.count(i):
            answer = length.count(i)
        i += 1
    return answer