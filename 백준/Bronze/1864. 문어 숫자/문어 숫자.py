d = { '-':0,
      '\\':1,
      '(':2,
      '@':3,
      '?':4,
      '>':5,
      '&':6,
      '%':7,
      '/':-1}

while True:
    s = input()

    if s == '#':
        break
    else:
        sum_all = 0
        n = len(s)-1
        for i in range(len(s)):
            sum_all += d[s[i]]*(8**n)
            n -=1
        print(sum_all)

