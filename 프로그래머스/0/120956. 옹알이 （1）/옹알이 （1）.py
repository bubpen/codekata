def solution(babbling):
    answer = 0
    baby = ["aya", "ye", "woo", "ma"]
    for word in babbling:
        for b in baby:
            if b in word:
                word = word.replace(b,' ')
                if word.replace(' ', '') == '':
                    answer +=1
                    break
    return answer