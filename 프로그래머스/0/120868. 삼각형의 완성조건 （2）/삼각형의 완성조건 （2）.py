def solution(sides):
    answer = 0
    i = 1
    a = max(sides)
    b = min(sides)
    s = a+b
    c = a-b
    while i < s:
        if i>c and i <s:
            answer+=1
        i +=1
    return answer