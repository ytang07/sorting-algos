def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            print(f"Comparing indicies {j} and {j+1}")
            print(f"The value in index {j} is {arr[j]}")
            print(f"The value in index {j+1} is {arr[j+1]}")
            if arr[j] > arr[j+1]:
                print(f"The value in index {j} is higher so we'll swap the values")
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(f"The array is now {arr} \n")

array = list(map(int, input("Input a list of numbers (separated by spaces)").split()))
print(f"Starting array is {array} \n")
bubble_sort(array)
print(f"Sorted array is {array}")