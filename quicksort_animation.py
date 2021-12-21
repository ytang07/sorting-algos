from animate_generator import animate
import random

def quicksort(array, start, end):
    if start >= end:
        return
    pivot = array[start]
    swap = start
    for i in range(start+1, end+1):
        if array[i] <= pivot:
            swap += 1
            array[swap], array[i] = array[i], array[swap]
        yield array
    array[start], array[swap],  = array[swap], array[start]
    yield array

    yield from quicksort(array, start, swap-1)
    yield from quicksort(array, swap+1, end)

array = [i for i in range(100)]
random.shuffle(array)
animate(array, quicksort(array, 0, 99), "quicksort", False)