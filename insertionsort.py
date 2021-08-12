def insertion_sort(_list):
    for i in range(len(_list)-1):
        print("The reference index is", i)
        j = i
        print("The current index is", j)
        _next = _list[i+1]
        print("The value of the next element is", _next)
        while _list[j] > _next and j >= 0:
            print(f"The value of the current index ({_list[j]}) is greater than {_next}")
            print("We will decrement our current index and swap the values in indices", j+1, "and", j)
            _list[j+1] = _list[j]
            j -= 1
            print("The current index is now", j)
        _list[j+1] = _next
        print(f"The value in the current index ({_list[j]}) is less than the value of next element, next iteration \n")
        print(f"The current state of the array is {_list}")
    return _list

array = list(map(int, input("Input a list of numbers (separated by spaces)").split()))
print("Starting array is", array)
insertion_sort(array)
print("Sorted array is", array)