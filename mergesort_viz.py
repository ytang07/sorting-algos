from animate_generator import animate
import random


def sort(_arr, start, end):
    if end <= start:
        return
    mid = start + ((end-start+1)//2)
    yield from sort(_arr, start, mid-1)
    yield from sort(_arr, mid, end)
    yield from merge(_arr, start, mid-1, end)
    yield _arr

def merge(_arr, start, mid, end):
    result = []
    left_index = start
    right_index = mid + 1
    while left_index <= mid and right_index <= end:
        if _arr[left_index] < _arr[right_index]:
            result.append(_arr[left_index])
            left_index+=1
        else:
            result.append(_arr[right_index])
            right_index+=1
    
    while left_index <= mid:
        result.append(_arr[left_index])
        left_index+=1
    
    while right_index <= end:
        result.append(_arr[right_index])
        right_index+=1
    
    for index, value in enumerate(result):
        _arr[start+index] = value
        yield _arr

N=100
array = [i for i in range(N)]
random.shuffle(array)
animate(array, sort(array, 0, N-1), "merge sort", True)