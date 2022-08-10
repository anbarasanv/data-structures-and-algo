def isValidSubsequence(array, sequence):
    # Write your code here.
    array_idx = 0
    seq_idx = 0
    while array_idx < len(array) and seq_idx < len(sequence):
        if array[array_idx] == sequence[seq_idx]:
            seq_idx += 1
        array_idx += 1
    return seq_idx == len(sequence)
