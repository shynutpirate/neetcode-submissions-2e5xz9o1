class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        
        res = 0

        for R in range(1, len(prices)):

            if prices[L] < prices[R]:
                res = max(res, prices[R] - prices[L])
            else:
                L = R
        return res
        