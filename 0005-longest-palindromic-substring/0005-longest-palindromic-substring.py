class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(substring: str) -> bool:
            return substring == substring[::-1]

        longest = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j+1]
                if is_palindrome(substring) and len(substring) > len(longest):
                    longest = substring

        return longest
