def solution(n, m):
    answer = []
    if n == m:
        for i in range(2):
            answer.append(n)
    else:
        a = min(n,m)
        b = max(n,m)
        div = []
        for num in range(1,a+1):
            if a % num == 0:
                div.insert(0,num)
        for num in div:
            if b % num == 0:
                answer.append(num)
                break
        answer.append((a*b)//answer[0])
        return answer