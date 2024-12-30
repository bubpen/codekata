def solution(bin1, bin2):
    l1 = len(bin1)-1
    a1 =0
    l2 = len(bin2)-1
    a2 = 0
    for i in bin1:
        a1 += int(i)*(2**l1)
        l1 -=1
    for i in bin2:
        a2 += int(i)*(2**l2)
        l2-=1
    b = a1 + a2
    c = format(b, 'b')
    return str(c)