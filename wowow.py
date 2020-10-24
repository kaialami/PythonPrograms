dic = {}
dic2 = {}
for x in range(10):
    dic[x] = '10'
print(dic)

for x in range(10):
    pee = dic.get(x)
    while pee in dic2:
        pee = 'w' + pee
    print(pee)
    dic2[x] = pee


print(dic2)