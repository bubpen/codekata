def solution(n):
    string = ''
    n_str = str(n)
    for i in n_str:
        string = i + string
    answer = []
    for i in string:
        answer.append(int(i))
    return answer