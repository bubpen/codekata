def solution(spell, dic):
    cnt = []
    alright = []
    for i in range(len(dic)):
        cnt.append([])
    for i in spell:
        alright.append(1)
        for j in range(len(dic)):
            cnt[j].append(dic[j].count(i))
    if alright in cnt:
        return 1
    else:
        return 2