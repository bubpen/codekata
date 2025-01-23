def solution(a, b):
    answer = ''
    days = 0
    day = ['THU', "FRI","SAT",'SUN','MON','TUE','WED']
    m31 = [1,3,5,7,8,10,12]
    m30 = [4,6,9,11]
    for m in range(1,a):
        if m in m31:
            days += 31
        elif m in m30:
            days += 30
        else:
            days += 29
    days+= b
    answer = day[days%7]
        
    return answer