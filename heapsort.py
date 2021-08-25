def heap(arr, n, i):
    print(f"Heaping on index {i}")
    root = i 
    lc = 2*i + 1
    rc = 2*i + 2
    if lc < n  and arr[i] < arr[lc]:
        print(f"Swapping left child, {arr[lc]}, and root, {arr[i]}")
        root = lc
    if rc < n and arr[root] < arr[rc]:
        print(f"Swapping right child, {arr[rc]}, and root, {arr[root]}")
        root = rc
    if root != i:
        arr[i], arr[root] = arr[root], arr[i]
        print(f"Array is now {arr} \n")
        heap(arr, n, root)

def heap_sort(arr):
    n = len(arr)
    for i in range(n//2, -1, -1):
        heap(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heap(arr, i, 0)

array = list(map(int, input("Input a list of numbers (separated by spaces)").split()))
print(f"Starting array is {array} \n")
heap_sort(array)
print(f"Sorted array is {array}")