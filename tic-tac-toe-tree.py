board = [0, 0, 0,
         0, 0, 0,
         0, 0, 0]

x = "x"
o = "o"

pos = {"tl":'', "ml":'', "bl":'', "tm":'', 'mm':'', 'bm':'', 'tr':'', 'mr':'', 'br':''}

branch_tl = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[]}

for n in range(8):
    branch = []
    for key, value in branch_tl.items():
        if n != key:
            if key % 2 == 0:
                value = x
            else:
                value = o
            branch.append({key:value})
    branch_tl[n] = branch

print(branch_tl)

