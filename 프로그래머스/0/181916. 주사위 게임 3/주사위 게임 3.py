def solution(a, b, c, d):
    n_list = list((a,b,c,d))
    n_set = set(n_list)
    if len(n_set) == 1:
        answer = list(n_set)[0] * 1111
    elif len(n_set) == 2:
        max_num, min_num = max(n_set), min(n_set)
        if n_list.count(max_num) == 3:
            answer = (10 * max_num + min_num)**2
        elif n_list.count(min_num) == 3:
            answer = (10 * min_num + max_num)**2
        else:
            answer = (max_num + min_num) * abs(max_num - min_num)
    elif len(n_set) == 3:
        if n_list.count(list(n_set)[0]) == 2:
            answer = list(n_set)[1] * list(n_set)[2]
        elif n_list.count(list(n_set)[1]) == 2:
            answer = list(n_set)[0] * list(n_set)[2]  
        else:
            answer = list(n_set)[1] * list(n_set)[0]
    else:
        answer = min(n_list)
    return answer