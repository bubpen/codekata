a,b = input().split()
r_a = ''
r_b = ''
for i in a:
    r_a = i + r_a
for i in b:
    r_b = i + r_b
print(max(int(r_a),int(r_b)))