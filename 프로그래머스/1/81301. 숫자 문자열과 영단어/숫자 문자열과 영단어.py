def solution(s):
    num_list = ['zero', 'one','two','three','four','five','six','seven','eight','nine']
    answer = ''
    word = ''
    for i in s:
        if i.isdigit():
            answer = answer + i
        else:
            word = word + i
            if word in num_list:
                answer = answer + str(num_list.index(word))
                word = ''
    return int(answer)