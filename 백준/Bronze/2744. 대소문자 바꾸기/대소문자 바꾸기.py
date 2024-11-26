s = input()
l = []
for i in range(len(s)):
    if s[i] == s[i].lower():
        l.append(s[i].upper())
    elif s[i]==s[i].upper():
        l.append(s[i].lower())
print(''.join(l))