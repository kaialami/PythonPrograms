import random, time

start = time.time()

# Big O: n^2
# Big omega: n^2
# Big theta: n
def bubbleSort(lst):
    result = lst
    size = len(result)
       
    for n in range(size - 1):
        finished = True
                
        for i in range(size - 1):
            if result[i] > result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]
                finished = False
            
            
        if finished == True:
            break
    
    return result


# Big O: n^2
# Big omega: n^2
# Big theta: n
def insertionSort(lst):
    result = lst
    size = len(result)
    
    for i in range(size):
        while i > 0 and result[i - 1] > result[i]:
            result[i], result[i - 1] = result[i - 1], result[i]
            i = i - 1
            
    return result


def selectionSort(lst):
    result = lst
    size = len(result)
    
    for i in range(size):
        minimum = i
        for j in range(size):
            if j >= i:
                if result[j] < result[minimum]:
                    minimum = j

        if minimum != i:
            result[minimum], result[i] = result[i], result[minimum]

    return result


def mergeSort(lst):
    result = lst
    size = len(result)
    half = int(size/2)
    if size == 1:
        return result
    

    l1 = lst[:half]
    l2 = lst[half:]
    
    return merge(mergeSort(l1), mergeSort(l2))

def merge(lst1, lst2):
    lst3 = []
    while len(lst1) > 0 and len(lst2) > 0:
        a = lst1[0]
        b = lst2[0]
        if a > b:
            lst3.append(b)
            lst2.remove(b)
        else:
            lst3.append(a)
            lst1.remove(a)

    while len(lst1) > 0:
        a = lst1[0]
        lst3.append(a)
        lst1.remove(a)
    while len(lst2) > 0:
        b = lst2[0]
        lst3.append(b)
        lst2.remove(b)

    return lst3


 

unsortedList = []

for i in range(100):
    unsortedList.append(random.randint(-99, 99))
    # unsortedList.append(i + 1)
 

print(unsortedList)


sortedList = mergeSort(unsortedList)
print('')
print(sortedList)
# print(bubbleSort(unsortedList))
print(sorted(unsortedList) == sortedList)
    

end = time.time()

print('\nFinished in', str(end - start),'seconds')