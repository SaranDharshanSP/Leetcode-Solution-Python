class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum = 0
        for row in accounts:
             if sum(row) > maximum:
                 maximum = sum(row)
        return maximum

