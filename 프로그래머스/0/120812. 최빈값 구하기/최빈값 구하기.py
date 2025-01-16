def solution(array):
    frequency = {}
    for num in array:
        frequency[num] = frequency.get(num,0) +1
    
    max_freq = max(frequency.values())
    number = []
    for key, value in frequency.items():
        if value == max_freq:
            number.append(key)
    if len(number) > 1:
        return -1
    else:
        return number[0]