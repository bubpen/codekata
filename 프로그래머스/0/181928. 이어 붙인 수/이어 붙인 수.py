def solution(num_list):
    odd_concat = ''
    even_concat = ''
    for i in num_list:
        if i % 2 == 0:
            even_concat = even_concat + str(i)
        else:
            odd_concat = odd_concat + str(i)
    return int(odd_concat) + int(even_concat)