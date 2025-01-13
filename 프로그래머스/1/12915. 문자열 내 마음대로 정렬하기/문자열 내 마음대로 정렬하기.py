def solution(strings, n):
    answer = []
    array= sorted([i[n] for i in strings])
    seted_array = set(array)
    for i in array:
        if array.count(i) == 1:
            for word in strings:
                if word[n] == i and word not in answer:
                    answer.append(word)
        else:
            duplicate = []
            for word in strings:
                if word[n] == i and word not in duplicate:
                    duplicate.append(word)
            duplicate.sort()
            for word in duplicate:
                if word not in answer:
                    answer.append(word)
    return answer