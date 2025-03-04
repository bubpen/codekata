def solution(babbling):
    answer = 0
    baby = [ "aya", "ye", "woo", "ma"]
    cant = ["ayaaya", "yeye", "woowoo", "mama"]
    for word in babbling:
        can = True
        for no in cant:
            if no in word:
                can = False
        if can:
            for _ in baby:
                if _ in word:
                    word = word.replace(_,' ')
                if word.replace(' ','') == '':
                    answer += 1
                    break
    return answer