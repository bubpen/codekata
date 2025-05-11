code = input()
n = int(input())
dictionary = []
found = False
for _ in range(n):
    dictionary.append(input())
new_code = ''
for shift in range(0, 25):
    new_code = ''
    for char in code:
        new_word = chr(ord(char)-shift)
        if ord(new_word) < 97:
            new_word = chr(ord(new_word) + 26)
        new_code += new_word
    for word in dictionary:
        if word in new_code:
            found = True
            break
    if found:
        break
print(new_code)