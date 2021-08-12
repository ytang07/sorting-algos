def pivot(array, start, end):
    pivot = array[start]
    left = start + 1
    right = end
    print("Pivot number is", pivot)
    print("Starting left and right indices are", left, "and", right)
    while True:
        while left <= right and array[right] >= pivot:
            right = right-1
            print(array[right+1], "is greater than or equal to", pivot, "so we shift the right index left to", right)
        while left <= right and array[left] <= pivot:
            left = left+1
            print(array[left-1], "is less than or equal to", pivot, "so we shift the left index right to", left)
        if left <=right:
            print("The left index is still on the left of the right index, so we'll swap the values")
            array[left], array[right] = array[right], array[left]
        else:
            print("The left index is further right than the right index so we don't need to swap")
            break
    
    print("We'll swap the values in indices", start, "and", right)
    array[start], array[right] = array[right], array[start]
    print("The array is now", array)
    return right

def quicksort(array, start, end):
    if start>=end:
        return
    p = pivot(array, start, end)
    quicksort(array, start, p-1)
    quicksort(array, p+1, end)

array = list(map(int, input("Input a list of numbers (separated by spaces)").split()))
print("Starting array is", array)
quicksort(array, 0, len(array)-1)
print(array)