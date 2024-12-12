def solution(n):
    duo =[]
    for i in range(1,n+1):
        if n % i == 0:
            duo.append((i,int(n/i)))
    return len(duo)