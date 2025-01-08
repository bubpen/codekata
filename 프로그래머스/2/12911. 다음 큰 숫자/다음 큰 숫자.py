def solution(n):
    bn = format(n, 'b')
    b = n + 1
    while True:
        bb = format(b, 'b')
        if bn.count('1') == bb.count('1'):
            answer = b
            break
        else:
            b += 1
    return answer