# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO

    # Made counters for each array

    i, j, k = 0, 0, 0

    # arrA = 1st array = i
    # arrB = 2nd array = j
    # merged_arr = combined array = k

    #
    while i < len(arrA) and j < len(arrB):

        # Checks to see if value of element in array A is smaller than value in element B
        # If it is, will append to combined array then increment up
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            k += 1
            i += 1
        else:
            merged_arr[k] = arrB[j]
            k += 1
            j += 1

    # Goes through rest of elements of each array
    # Goes through 1st array
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        k += 1
        i += 1

    # Goes through 2nd array
    while j < len(arrB):
        merged_arr[k] = arrB[j]
        k += 1
        j += 1

    # print(merged_arr)
    return merged_arr

Arr1 = [1,3,5]
Arr2 = [2,4]

print(merge(Arr1, Arr2))


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO

    # Base case
    if len(arr) <= 1:
        return arr

    # Length of array
    arr_length = len(arr)

    # Finds the middle element
    middle = arr_length // 2

    # Sorts everything on the left
    sorted_left = merge_sort(arr[:middle])

    # Sorts everything on right
    sorted_right = merge_sort(arr[middle:])

    # Merge both sorted array here
    arr = merge(sorted_left, sorted_right)

    return arr

arr3 = [1, 4, 5, 2, 3]
print(merge_sort(arr3))



# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
