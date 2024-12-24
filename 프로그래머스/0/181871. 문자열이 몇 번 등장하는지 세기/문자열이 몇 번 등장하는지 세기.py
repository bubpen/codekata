def solution(myString, pat):
    l = len(pat)
    cnt = 0
    for i in range(len(myString)-l+1):
        if pat == myString[i:i+l]:
            cnt += 1 
    return cnt