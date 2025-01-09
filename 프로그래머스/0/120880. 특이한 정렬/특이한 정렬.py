def solution(numlist, n):
    sublist = [abs(x - n) for x in numlist]
    answer = []
    diff = 0
    while True:
        cnt = sublist.count(diff)
        for i in range(cnt):
            if n+diff in numlist and answer.count(n+diff) < numlist.count(n+diff):
                answer.append(n+diff)
            else:
                answer.append(n-diff)
        if len(answer) == len(numlist):
            break
        else:
            diff += 1
    return answer