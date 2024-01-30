class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans =[]
        for candy in candies:
           ans.append(extraCandies + candy >= max(candies))
        return ans    
