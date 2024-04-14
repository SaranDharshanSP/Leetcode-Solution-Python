import sys
sys.set_int_max_str_digits(0)
class Solution:
    def largestOddNumber(self, num: str) -> str:
        if int(num) % 2 != 0: return num
        for i in range(len(num)-1,-1,-1):
             if int(num[i])% 2 != 0: return num[:i+1]
        return ''
