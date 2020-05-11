# Remove Duplicates from Sorted Array

## Best Time to Buy And Sell Stock II
def max_profit(prices):
    if len(prices) <= 1:
        return 0
    
    profit = 0
    slow = 0

    while prices[slow+1] < prices[slow]:
        if slow == len(prices) - 1:
            return profit
        else:
            slow += 1

    
    prev_fast = slow
    fast = slow + 1

    while fast < len(prices):
        if prices[fast] > prices[slow]:
            print('if')
            print('slow', slow)
            print('prev_fast', prev_fast)
            print('fast', fast)
            if fast == len(prices) - 1:
                print('ifif')
                print(f'{prices[fast]} - {prices[slow]}')
                profit += (prices[fast] - prices[slow])
                return profit
        elif prices[fast] < prices[slow]:
            print('elif')
            if fast == len(prices) - 1:
                print('elifif')
                print(f'prices[fast]: {prices[fast]}, prices[slow]: {prices[slow]}')
                return profit
            elif prev_fast != 0 & prices[prev_fast] > prices[slow]:
                print('elifelif')
                profit += (prices[prev_fast] - prices[slow])
                slow = fast
        fast += 1
        prev_fast += 1
    
print(max_profit([1,2,3,4,5]))
print('-------------------')
print(max_profit([7,6,4,3,1]))
print('-------------------')
print(max_profit([7,1,5,3,6,4]))
