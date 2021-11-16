# Sorting Techniques

import sys
A = [5,3,2,4,1]

for i in range(len(A)):
    min_indx = i
    for j in range(i+1, len(A)):
        if A[min_indx] > A[j]:
            min_indx = j
    A[i], A[min_indx] = A[min_indx], A[i]

print('Sorted Array')
for i in range(len(A)):
    print("%d" %A[i])

#Selection Sort

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [5,3,2,4,1]
bubbleSort(arr)

print('Sorted Array')
for i in range(len(A)):
    print("%d" %A[i])

#Bubble Sort

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

arr = [5,3,2,4,1]
insertionSort(arr)

print('Sorted Array')
for i in range(len(A)):
    print("%d" %A[i])

#Insertion Sort

import sys
def partition(arr,low,high):
    i = (low-1)
    pivot = arr[high]
    for j in range(low,high):
        if arr[j] < pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1],arr[high] = arr[high], arr[i+1]
    return (i+1)

def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)

arr = [5,3,2,4,1]
n = len(arr)
quickSort(arr,0,n-1)

print('Sorted Array')
for i in range(len(A)):
    print("%d" %A[i])

#Quick Sort

def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        l = arr[:mid]
        r = arr[mid:]
        mergeSort(l)
        mergeSort(r)
        i = j = k = 0

        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                arr[k] = l[i]
                i+=1
            else:
                arr[k] = r[j]
                j+=1
            k+=1

        while i < len(l):
            arr[k] = l[i]
            i+=1
            k+=1

        while j < len(r):
            arr[k] = r[j]
            j+=1
            k+=1

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end= " ")
    print()

arr = [5,3,2,4,1]
print("Given: ", end="\n")
printList(arr)
mergeSort(arr)
print("Sorted: ", end="\n")
printList(arr)

#Merge Sort

def heapify(arr,n,i):
    largest = i
    l = 2*i+1
    r = 2*i+2

    if l < n and arr[i]<arr[l]:
        largest = 1
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i],arr[largest] = arr[largest], arr[i]
        heapify(arr,n,largest)
def heapSort(arr):
    n = len(arr)
    for i in range(n,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[i], arr[0] = arr[0],arr[i]
        heapify(arr,i,0)

arr = [5,3,2,4,1]
heapSort(arr)
n = len(arr)
print("Sorted is:")
for i in range(len(A)):
    print("%d" %A[i])

#Heap Sort
