class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, best = 0, 1, 0
        for i in range(1, len(prices)):
            r = i
            if prices[l] < prices[r]:
                best = max(best, prices[r] - prices[l])
            else:
                l = r
        return best