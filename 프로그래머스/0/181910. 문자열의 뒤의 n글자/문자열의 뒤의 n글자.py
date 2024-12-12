def solution(my_string, n):
    i = -1
    answer = ''
    while i >= -n:
        answer = my_string[i] + answer
        i -= 1
    return answer