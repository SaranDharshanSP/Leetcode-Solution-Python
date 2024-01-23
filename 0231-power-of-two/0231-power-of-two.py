import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return (n>0 and ((math.log10(n)/math.log10(2))%1==0))