def solution(n):
    i = 1
    b = 1
    while True:
        b *= i
        i += 1
        if b == n or n -b*i < 0:
            return i-1
        