def maxProfit(prices: [int]) -> int:
    l, r = 0, 1
    mp = 0
    while r < len(prices):
        p = prices[r]-prices[l]

        if prices[l] > prices[r]:
            l = r
        r += 1

        if p > mp:
            mp = p
    return mp


# Alternative solution:
"""
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        low = INT_MAX
        for p in prices:
            if p < low:
                low = p
            c = p - low
            if c > best:
                best = c
        return best
            
"""