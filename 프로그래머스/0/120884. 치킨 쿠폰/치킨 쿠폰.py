def solution(chicken):
    coupon = chicken
    service = 0
    answer = 0
    while coupon >= 10:
        answer += coupon // 10
        service = coupon // 10
        coupon -= service * 9

    return answer