def solution(a, b):
    if a == b or a % b == 0:
        answer = 1
    else:
        n = min(a,b)
        m = max(a,b)
        div = []
        for i in range(1,n+1):
            if n % i == 0:
                div.insert(0,i)
        for i in div:
            if m % i == 0:
                gcd = i
                break
        b = b //gcd
        answer = 1
        d = 2
        if b == 2 or b == 5:
            answer = 1
        else:
            while b > 1 and d <= b:
                if b % d == 0:
                    if d != 2 and d != 5:
                        answer = 2
                        break
                    else:
                        b //=d
                else:
                     d += 1   
    return answer