class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        for i in operations:
            if i.lstrip('-').isdigit():stk.append(int(i))
            if i =='C':stk.pop()
            if i == 'D': stk.append(int(stk[-1])*2)
            if i == '+':stk.append(int(stk[-1])+int(stk[-2]))
        return sum(stk)
