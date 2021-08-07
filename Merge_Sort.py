def mergeSort(array, start, end):
    if end - start > 1:
        middle = (start + end) //2
        mergeSort(array, start, middle)
        mergeSort(array, middle, end)
        merge(array, start, middle, middle, end)

def merge(array, left, leftEnd, right, rightEnd):
    while left<leftEnd and right<rightEnd:
        if array[left] > array[right]:
            array.insert(left, array.pop(right))
            right += 1
            leftEnd += 1
        else:
            left += 1
            

import random
data = [4,9,7,2,3,10,6,1]
mergeSort(data, 0, len(data))
print(data)
