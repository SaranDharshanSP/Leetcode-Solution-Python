class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        br = { ')':'(', '}':'{',']':'['}
        for i in s:
            if i in br:
                if stk and stk[-1] == br[i]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(i)
        return True if not stk else False
            
       