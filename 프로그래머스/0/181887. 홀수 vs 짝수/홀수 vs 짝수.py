def solution(num_list):
    answer = 0
    odd_sum = 0
    even_sum = 0
    for i in range(len(num_list)):
        if (i+1) % 2 == 1:
            odd_sum += num_list[i]
        else:
            even_sum += num_list[i]
    answer = max(odd_sum, even_sum)
    return answer