def solution(my_string, n):
    string = []
    for i in my_string:
        for j in range(0,n):
            string.append(i)
    return ''.join(string)