string = input().upper()
w_cnt = {}
for i in string:
    w_cnt[i] = w_cnt.get(i,0)+1
m_c = max(w_cnt.values())
m_w = []
for i in w_cnt.keys():
    if w_cnt[i] == m_c:
        m_w.append(i)
if len(m_w) != 1 :
    print('?')
else:
    print(m_w[0])