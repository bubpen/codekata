def solution(my_string, overwrite_string, s):
    answer = my_string[:s]+overwrite_string
    if len(answer) < len(my_string):
        answer = answer + my_string[len(answer):]
    return answer