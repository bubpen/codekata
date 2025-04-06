def solution(topping):
    answer = 0
    left_set = set()
    right_dict = dict()
    for t in topping:
        right_dict[t] = right_dict.get(t,0) +1
    
    for t in topping:
        left_set.add(t)
        right_dict[t] -= 1
        if right_dict[t] == 0:
            del right_dict[t]
        if len(left_set) == len(right_dict):
            answer += 1
    return answer