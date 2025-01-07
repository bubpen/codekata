def solution(number):
    answer = 0
    for f in range(len(number)-2):
        for s in range(f+1,len(number)-1):
            for t in range(s+1,len(number)):
                if number[f]+number[s]+number[t] == 0:
                    answer += 1
    return answer