def solution(rank, attendance):
    member = []
    for i in range(len(rank)):
        if attendance[i]:
          member.append(rank[i])
    member.sort()
    answer = rank.index(member[0]) * 10000 + rank.index(member[1]) * 100 + rank.index(member[2])
    return answer