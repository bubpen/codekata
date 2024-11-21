def solution(my_str, n):
    answer = []
    a = ''
    for i in range(len(my_str)):
        a = a+my_str[i]
        if len(a)==n or i == len(my_str)-1:
            answer.append(a)
            a = ''
            
    return answer