def solution(date1, date2):
    answer = 0
    if date1[0] > date2[0]:
        pass
    elif date1[0] == date2[0] and date1[1]> date2[1]:
        pass
    elif date1[0] == date2[0] and date1[1] == date2[1] and date1[2] >= date2[2]:
        pass
    else:
        answer = 1
    return answer