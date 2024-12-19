def solution(my_string):
    l = []
    for i in my_string:
        if i not in ['1','2','3','4','5','6','7','8','9','0']:
            pass
        else:
            l.append(int(i))
    l.sort()
    return l