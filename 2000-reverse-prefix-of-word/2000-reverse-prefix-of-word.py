class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:return word
        for i in range(len(word)):
            if word[i] == ch:
                return word[i::-1]+word[i+1:]
