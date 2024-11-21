def solution(s):
    l = list(s)
    l.sort()
    answer = ''
    cnt = {}
    for i in l:
        cnt[i] = cnt.get(i,0)+1
    for i in cnt.keys():
        if cnt[i] ==1:
            answer = answer+i
    return answer