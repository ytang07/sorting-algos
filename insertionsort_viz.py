from animate_generator import animate
import random

def insertion_sort(_list):
    for i in range(1, len(_list)):
        j = i-1
        next = _list[i]
        while _list[j] > next and j >= 0:
            _list[j+1] = _list[j]
            j -= 1
            yield _list
        _list[j+1] = next
        yield _list

array = [i for i in range(50)]
random.shuffle(array)
animate(array, insertion_sort(array), "insertion sort", True)