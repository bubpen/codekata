def solution(num, k):
    a = []
    for i in str(num):
        a.append(int(i))
    if not str(k) in str(num):
        return -1
    for i in a:
        if i == k:
            answer = a.index(i)+1
            break
        
    return answer