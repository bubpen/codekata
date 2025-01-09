def solution(s, n):
    low_alp = 'abcdefghijklmnopqrstuvwxyz'
    up_alp = low_alp.upper()
    s_list = [x for x in s]
    answer = []
    for word in s_list:
        if word in low_alp:
            i = low_alp.index(word) + n
            answer.append(low_alp[i%26])
        elif word in up_alp:
            i = up_alp.index(word) + n
            answer.append(up_alp[i % 26])
        else:
            answer.append(' ')
    return ''.join(answer)