str = input()
a=''
for i in str:
    if i == i.upper():
        a = a+i.lower()
    else:
        a = a+i.upper()
print(a)