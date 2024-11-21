def solution(array):
    a = ''
    for i in array:
        a = a + str(i)
    b = list(a)
    return b.count('7')