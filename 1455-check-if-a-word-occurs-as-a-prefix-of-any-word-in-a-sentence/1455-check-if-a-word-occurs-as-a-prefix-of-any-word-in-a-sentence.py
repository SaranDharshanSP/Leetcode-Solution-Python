class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        s = list(sentence.split(" "))
        r=len(searchWord)
        for i in range(len(s)):
            if searchWord in s[i] and searchWord == s[i][0:r] :return i+1
        return -1