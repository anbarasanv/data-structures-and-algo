def sortedSquaredArray(array):
    # Write your code here.
    arr_len = len(array)
    left = 0
    right = arr_len-1
    result = [0] * arr_len
    while left <= right:
        arr_len -= 1
        if abs(array[left]) > abs(array[right]):
            result[arr_len] = array[left]**2
            left += 1
        elif abs(array[left]) <= abs(array[right]):
            result[arr_len] = array[right]**2
            right -= 1
    return result
