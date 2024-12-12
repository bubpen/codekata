def solution(my_string):
    answer = ''
    bowel = ['a','e','i','o','u']
    for i in my_string:
        if i not in bowel:
            answer = answer + i
    return answer