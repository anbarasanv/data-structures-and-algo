# Time: O(n log n) | Space: O(n)
def sortedSquaredArray(array):
    # Write your code here.
    array = [item**2 for item in array]
    return sorted(array)
