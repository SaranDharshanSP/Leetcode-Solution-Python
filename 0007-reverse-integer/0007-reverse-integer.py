class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x = abs(x)
        ab = ''
        
        for i in range(len(str(x))):
            a = str((x//10**i) %10)
            ab+=a
        rev = sign * int(ab)

        if rev < -2**31 or rev > 2**31 - 1:return 0
        else:return rev   