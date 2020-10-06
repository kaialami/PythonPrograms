dic = {}

for i in range(10):
    dic[i] = i**2

print(dic)

for x, y in dic.items():
    print(x * y)