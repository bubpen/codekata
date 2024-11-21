def solution(before, after):
    a = []
    for i in before:
        if before.count(i)==after.count(i):
            a.append(1)
        else:
            a.append(0)
    if a.count(1)==len(before):
        return 1
    else:
        return 0