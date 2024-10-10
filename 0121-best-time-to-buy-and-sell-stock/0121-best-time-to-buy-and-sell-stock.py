class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low,res = prices[0], 0
        for i in prices:
            low = min(low,i)
            res =  max(res, i-low)
        return res