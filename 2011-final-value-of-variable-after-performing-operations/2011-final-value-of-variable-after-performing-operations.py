class Solution:
    def finalValueAfterOperations(self, op: List[str]) -> int:
        ans = 0
        for x in op:
            if x[1] == "+":
                ans += 1    
            else:
                ans -= 1
        return ans