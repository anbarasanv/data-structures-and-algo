def isValidSubsequence(array, sequence):
    len_sequence = len(sequence)
    count = 0
    for element in array:
        if element == sequence[count]:
            count += 1
            len_sequence -= 1
        if len_sequence <= 0:
            return True
    return False
