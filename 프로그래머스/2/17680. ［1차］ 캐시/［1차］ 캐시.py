def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        if city.lower() in cache:
            answer += 1
            cache.pop(cache.index(city.lower()))
        else:
            answer += 5
        cache.append(city.lower())
        if len(cache) > cacheSize:
            cache = cache[1:]
    return answer