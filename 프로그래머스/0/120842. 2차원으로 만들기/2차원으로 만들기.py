def solution(num_list, n):
    answer = []
    for i in range(0,len(num_list),n):
        r = []
        for j in range(n):
            r.append(num_list[i+j])
        answer.append(r)
    return answer