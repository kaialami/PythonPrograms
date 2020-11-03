def binaryTree(lst):
    size = len(lst)
    if size < 3:
        if size == 2:
            return [lst[1], [lst[0], [], []], []]
        elif size == 1:
            return [lst[0], [], []]
        else:
            return None

    mid = size // 2
    parent = lst[mid]
    la = lst[:mid]
    ra = lst[mid + 1:]
    size_la = len(la)
    la_mid = size_la // 2
    la_parent = la[la_mid]
    size_ra = len(ra)
    ra_mid = size_ra // 2
    ra_parent = ra[ra_mid]
    la_count = size_la 
    ra_count = size_ra
    ret = [parent, la, ra]
    print(ret)

    # while la_count > 0:
    #     size_la = len(la)
    #     mid = size_la // 2
    #     parent = la[]

def unbalTree(lst):
    root = lst[0]
    parent = lst[0]
    la = []
    ra = []
    ret = []
    count = len(lst) - 1
    while count > 0:
        for x in range(1, len(lst)):
            if lst[x] < parent:
                la.append(lst[x])
            else:
                ra.append(lst[x])
        ret = [root, la, ra]
    print([parent, la, ra])
        

from random import randint
the_list = []
for x in range(7):
    the_list.append(randint(1, 20))

the_list.sort()
print(the_list)
print(unbalTree(the_list))