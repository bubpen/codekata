def solution(a, b, n):
    answer = 0
    while n >= a:
        re = n //a
        answer += re * b
        n = n - re*a + re*b
        
    return answer