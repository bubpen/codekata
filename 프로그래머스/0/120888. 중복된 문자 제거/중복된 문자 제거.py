def solution(my_string):
    answer = ''
    l = list(my_string)
    for i in my_string:
        if i in answer:
            pass
        else:
            answer = answer + i
    return answer