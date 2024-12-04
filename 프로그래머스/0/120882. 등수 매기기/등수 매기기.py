def solution(score):
    mean_score = []
    for i in range(len(score)):
        mean_score.append(sum(score[i])/len(score[i]))
    rank_list = sorted(mean_score, reverse = True)
    answer = []
    for i in range(len(score)):
        answer.append(rank_list.index(mean_score[i])+1)
    return answer