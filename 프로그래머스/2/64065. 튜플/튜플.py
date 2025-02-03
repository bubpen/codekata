def solution(s):
    answer = []
    num_list = []
    for i in s[1:len(s)-1]:
        if i == '{':
            num_list.append([])
            n = ''
        elif i.isdigit():
            n += i
        elif i == ',' and n != '':
            num_list[-1].append(int(n))
            n = ''
        elif i == '}':
            num_list[-1].append(int(n))
            n = ''
    num_list.sort(key = len)
    for l in num_list:
        for num in l:
            if num not in answer:
                answer.append(num)
                break
    return answer