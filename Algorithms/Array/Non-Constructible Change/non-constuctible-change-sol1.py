def nonConstructibleChange(coins):
    # Write your code here.
    min_sum = 0
    coins.sort()
    for coin in coins:
        if coin > min_sum+1:
            return min_sum+1
        min_sum += coin

    return min_sum+1
