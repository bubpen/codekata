def solution(n):
    answer = 0
    if n % 2 == 0:
        length = n//2
        cnt_two = n//2
        cnt_one = 0
    else:
        length = n//2 + 1
        cnt_two = n//2
        cnt_one = 1
    while length <= n:
        if cnt_one > 0:
            c1 =1
            p =1
            for i in range(1,cnt_one+1):
                c1 *= i
            for i in range(cnt_two+1,length+1):
                p *= i
            answer += p//c1
        else:
            answer += 1
        cnt_two -= 1
        cnt_one += 2
        length += 1
    return answer % 1234567