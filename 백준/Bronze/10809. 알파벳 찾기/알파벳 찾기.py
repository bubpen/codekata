string = input().lower()
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
locate = []
for i in alphabet:
    if i in string:
        locate.append(str(string.index(i)))
    else:
        locate.append('-1')
print(' '.join(locate))