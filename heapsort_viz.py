from animate_generator import animate
import random

def heap(arr, n, i):
    root = i 
    lc = 2*i + 1
    rc = 2*i + 2
    if lc < n  and arr[i] < arr[lc]:
        root = lc
    if rc < n and arr[root] < arr[rc]:
        root = rc
    if root != i:
        arr[i], arr[root] = arr[root], arr[i]
        heap(arr, n, root)

def heap_sort(arr):
    n = len(arr)
    for i in range(n//2, -1, -1):
        heap(arr, n, i)
        yield arr
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        yield arr
        heap(arr, i, 0)
        yield arr

array = [i for i in range(100)]
random.shuffle(array)
animate(array, heap_sort(array), "heap sort", False)