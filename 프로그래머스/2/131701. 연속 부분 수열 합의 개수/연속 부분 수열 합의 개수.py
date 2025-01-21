def solution(elements):
    length = len(elements)
    elements = elements * 2
    result = set()
    for i in range(length):
        for j in range(length):
            result.add(sum(elements[j:j+i+1]))
    return len(result)