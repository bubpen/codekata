def solution(num_list, n):
    answer = []
    for i in range(len(num_list)):
        answer.append(0)
    for i in range(len(num_list)):
        a = num_list[i]
        i -= n
        answer[i] = a
    return answer