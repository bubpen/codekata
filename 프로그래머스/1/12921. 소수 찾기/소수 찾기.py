def solution(n):
    answer = 0
    for i in range(2,n+1):
        div = 0
        for _ in range(1,int(i**0.5)+1):
            if i % _ == 0:
                div +=1
                if div >1:
                    break
        if div == 1:
            answer += 1
    return answer