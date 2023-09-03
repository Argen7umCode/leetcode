from itertools import combinations


def maxProfit(prices) -> int:
    if len(prices) < 2:
        return 0
    comb = combinations(prices, 2)
    return max([max(map(lambda a: a[1]-a[0], comb)), 0])

def maxProfit(prices) -> int:
    if len(prices) < 2:
        return 0
    min_el = float('inf')
    max_div = 0
    for el in prices:
        min_el = min([el, min_el])
        max_div = max([el-min_el, max_div])
    return max_div


assert maxProfit([7,1,5,3,6,4]) == 5
# assert maxProfit([7,6,4,3,1]) == 0
maxProfit([1])
