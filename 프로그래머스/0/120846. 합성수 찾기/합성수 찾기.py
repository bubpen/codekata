def solution(n):
    list = []
    i = 4
    while i <=n:
        cnt = 0
        for j in range(1,i+1):
            if i % j ==0:
                cnt += 1
        if cnt >2:
            list.append(i)
        i += 1
    return len(list)