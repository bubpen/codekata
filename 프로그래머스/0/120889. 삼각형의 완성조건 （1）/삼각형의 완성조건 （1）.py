def solution(sides):
    if max(sides)*2 - sum(sides)<0:
        return 1
    else:
        return 2