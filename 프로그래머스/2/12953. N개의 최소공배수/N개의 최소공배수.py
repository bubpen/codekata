def solution(arr):
    while len(arr)>=2:
        a = arr.pop()
        b = arr.pop()
        m = min(a,b)
        M = max(a,b)
        div = []
        for n in range(1,m+1):
            if m % n ==0:
                div.insert(0,n)
        for n in div:
            if M % n == 0:
                gcd = n
                break
        arr.append((m*M)//gcd)
    return arr[0]