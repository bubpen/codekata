def solution(N, stages):
    answer = list(range(1,N+1))
    player = len(stages)
    rate = []
    for stage in answer:
        if stages.count(stage) == 0:
            rate.append(0)
        else:
            rate.append(stages.count(stage)/player)
        player -= stages.count(stage)
    return [x for _,x in sorted(zip(rate,answer), key=lambda x: (-x[0], x[1]))]