def solution(want, number, discount):
    answer = 0
    length = len(want)
    for i in range(0, len(discount) - sum(number)+1):
        correct = 0
        for j in range(length):
            if discount[i:i+sum(number)].count(want[j]) != number[j]:
                break
            else:
                correct += 1
        if correct == length:
            answer += 1
    return answer