num = input()
a = []
for i in range(int(num)):
    name = input()
    a.append(name)
for el in a:
    if el not in 'абвАБВ':
        v = 'No'
        break
    else:
        v = 'Yes'
print(v)