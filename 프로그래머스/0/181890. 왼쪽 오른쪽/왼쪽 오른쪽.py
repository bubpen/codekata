def solution(str_list):
    answer = []
    if 'l' in str_list and 'r' in str_list: 
        if str_list.index('l') < str_list.index('r'):
            i = str_list.index('l')
            answer = str_list[:i]
        else:
            i = str_list.index('r')
            answer = str_list[i+1:]
    elif 'l' in str_list:
        i = str_list.index('l')
        answer = str_list[:i]
    elif 'r' in str_list:
        i = str_list.index('r')
        answer = str_list[i+1:]
    else:
        answer = []
    return answer