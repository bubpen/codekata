def solution(M, N):
    answer = 0
    cnt_m = 0
    cnt_n = 0
    while M != 1:
        cnt_m += 1
        M -= 1
    while N != 1:
        cnt_n += 1
        N -= 1
    answer = cnt_m + (cnt_m + 1) * cnt_n
    return answer