string = input()
croatia_str = ['c=', 'c-','dz=','d-','lj','nj','s=','z=']
cnt = 0
i = 0

while i < len(croatia_str):
    if croatia_str[i] in string:
        string = string.replace(croatia_str[i],' ',1)
        cnt +=1
        i = 0
    else:
        i +=1
    
s_l = list(string.replace(' ','').strip())
cnt += len(s_l)
print(cnt)