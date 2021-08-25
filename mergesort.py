def merge_sort(arr):
    n = len(arr)
    if n > 1:
        middle = n//2
        left = arr[:middle]
        right = arr[middle:]
        print(f"Array split into {left} and {right}")
        merge_sort(left)
        merge_sort(right)

        left_index = 0
        right_index = 0
        arr_index = 0
        left_size = len(left)
        right_size = len(right)

        print(f"Starting new merge for {arr}")
        # while both the left and right index counters are within the sizes of their respective arrays
        while left_index < left_size and right_index < right_size:
            # 
            if left[left_index] < right[right_index]:
                arr[arr_index] = left[left_index]
                left_index+=1
            else:
                arr[arr_index] = right[right_index]
                right_index+=1
            arr_index+=1
        
        while left_index < left_size:
            arr[arr_index] = left[left_index]
            left_index+=1
            arr_index+=1
        
        while right_index < right_size:
            arr[arr_index] = right[right_index]
            right_index+=1
            arr_index+=1
        
        print(f"Merge done - current array {arr}")

array = list(map(int, input("Input a list of numbers (separated by spaces)").split()))
print(f"Starting array is {array} \n")
merge_sort(array)
print(f"Sorted array is {array}")