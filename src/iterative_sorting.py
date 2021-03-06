# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i + 1] < arr[i]:
                swapped = True
                arr[i], arr[i + 1], = arr[i + 1], arr[i]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # return list if it doesn't need to be sorted
    if len(arr) <= 1:
        return arr

    # make a count array to store data
    count = [0 for i in range(max(arr) + 1)]

    # for each number in array, add one to the count array's entry
    for num in arr:
        # first check if num is negative, if so throw error
        if num < 0:
            return "Error, negative numbers not allowed in Count Sort"
        count[num] += 1

    # modify the array so that each element stores the sum of previous counts (therefore sorting the list)
    for idx in range(1, len(count)):
        count[idx] += count[idx - 1]

    # make an output array the same length as the input
    output = [0 for i in range(len(arr))]

    # build the output array
    for i in range(len(arr)):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    return output
