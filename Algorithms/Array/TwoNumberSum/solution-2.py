# O(n) time | O(n) space
def twoNumberSum(array, targetSum):
    nums = {}
    for number in array:
        expected_val = targetSum - number
        if expected_val in nums:
            return [expected_val, number]
        else:
            nums[number] = True
    return []
