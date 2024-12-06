final = ''
str_list = []
for i in range(5):
    string = input()
    str_list.append(string)
max_len = 0
for i in str_list:
    if len(i) > max_len:
        max_len = len(i)
for i in range(len(str_list)):
    if len(str_list[i]) < max_len:
        str_list[i] = str_list[i].replace(str_list[i],str_list[i]+' '*(max_len - len(str_list[i])))
for i in str_list:
    final = final + i
f_l = list(final)
n = 0
t = []
for i in range(max_len):
    t.append([])
    
while n < len(f_l):
    if f_l[n] == ' ':
        n += 1
        continue
    t[n%max_len].append(f_l[n])
    n += 1
answer = ''
for i in t:
    answer = answer + ''.join(i)
print(answer)