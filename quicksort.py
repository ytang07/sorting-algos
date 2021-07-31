def pivot(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end
    print("Pivot number is", pivot)
    print("Low index is", low)
    print("High index is", high)
    while True:
        while low <= high and array[high] >= pivot:
            high = high-1
            print(array[high+1], "is greater than or equal to", pivot, "the high index is now", high)
        while low <= high and array[low] <= pivot:
            low = low+1
            print(array[low-1], "is less than or equal to", pivot, "the low index is now", low)
        if low <=high:
            print("The low index is less than or equal to the high index, so we'll swap the values")
            array[low], array[high] = array[high], array[low]
        else:
            print("The low index is higher than the high index so we don't need to swap")
            break
    
    print("We'll swap", array[start], array[high], "the starting number and the number in the high index")
    array[start], array[high] = array[high], array[start]
    print("The high index is", high, "the low index is", low)
    return high

def quicksort(array, start, end):
    if start>=end:
        return
    p = pivot(array, start, end)
    quicksort(array, start, p-1)
    quicksort(array, p+1, end)

array = [5, 1, 3, 9, 8, 2, 7]
print("Starting array is", array)
quicksort(array, 0, len(array)-1)
print(array)
