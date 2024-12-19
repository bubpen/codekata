def solution(my_string):
    answer = []
    a = ''
    for i in range(1,len(my_string)+1):
        a = my_string[-i] + a
        answer.append(a)
    answer = sorted(answer)
    return answer