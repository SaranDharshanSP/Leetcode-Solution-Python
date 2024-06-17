class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        while 2 * a * a <=c:
            b = (c - a * a) ** 0.5
            if (a**2 + int(b)**2 == c):
                return True
            a+=1
        return False
