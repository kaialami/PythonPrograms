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
            

unsortedList = []
for i in range(10):
    unsortedList.append(random.randint(-99, 99))
 #   unsortedList.append(i + 1)
 

print(unsortedList)


sortedList = selectionSort(unsortedList)
print(sortedList)
#print(sorted(unsortedList))



end = time.time()

print('\nFinished in', str(end - start),'seconds')