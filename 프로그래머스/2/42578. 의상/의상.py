def solution(clothes):
    answer = 1
    closet = {}
    for cloth, kind in clothes:
        closet[kind] = closet.get(kind,0) +1
    for value in closet.values():
        answer *= value+1
    return answer-1