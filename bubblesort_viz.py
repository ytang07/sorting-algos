from animate_generator import animate
import random

def bubblesort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                yield arr

array = [i for i in range(50)]
random.shuffle(array)
animate(array, bubblesort(array), "bubble sort", True)