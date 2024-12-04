def solution(n):
    x3 = []
    num_list = range(1,n+1)
    i = 0
    while len(x3) < len(num_list):
        i += 1
        if '3' not in str(i) and i%3 != 0:
            x3.append(i)
        
    return i