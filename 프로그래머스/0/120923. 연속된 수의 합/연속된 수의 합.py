def solution(num, total):
    answer = []
    sigma = 0
    for n in range(1, num):
        sigma += n
    start = (total - sigma)//num
    n = 0
    answer = [start+i for i in range(num)]
    return answer