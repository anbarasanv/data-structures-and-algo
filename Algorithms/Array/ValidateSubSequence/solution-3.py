
def isValidSubsequence(array, sequence):
    len_sequence = len(sequence)
    count = 0
    for element in array:
        if count == len(sequence):
            break
        if element == sequence[count]:
            count += 1

    return len_sequence == count
