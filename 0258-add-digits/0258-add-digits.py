class Solution:
    def addDigits(self, num: int) -> int:
        num_str = str(num)
        digit_sum = 0
        for digit in num_str:
            digit_sum += int(digit)
        if digit_sum >= 10:
            return self.addDigits(digit_sum)
        else:
            return digit_sum
