def solution(my_string):
    a = ''
    for i in my_string:
        if i in ['1','2','3','4','5','6','7','8','9','0']:
            a = a+i
        else:
            a = a+ ' '
    l = list(map(int,a.split()))
    return sum(l)