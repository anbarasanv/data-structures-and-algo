# O(n^2) time | O(1) space

def two_number_sum(array, target_sum):
    range_val = len(array)
    result = []
    for i in range(range_val):
        for j in range(i+1, range_val):
            if sum([array[i], array[j]]) == target_sum:
                return [array[i], array[j]]
    return result
