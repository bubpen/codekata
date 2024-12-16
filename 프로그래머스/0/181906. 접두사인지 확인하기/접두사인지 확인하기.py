def solution(my_string, is_prefix):
    answer = 0
    if is_prefix == my_string[0:len(is_prefix)]:
        answer =1
    return answer