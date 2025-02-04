def solution(s):
    answer = 0
    l = s.split()
    return sum(int(l[i]) if l[i] != 'Z' else -int(l[i-1]) for i in range(len(l)))
