from itertools import permutations

def solution(k, dungeons):
    max_count = 0

    for perm in permutations(dungeons):
        stamina = k
        count = 0

        for min_required, cost in perm:
            if stamina >= min_required:
                stamina -= cost
                count += 1
            else:
                break

        max_count = max(max_count, count)

    return max_count