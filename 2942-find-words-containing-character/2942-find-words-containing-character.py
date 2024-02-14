class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        a = [] 
        for i,j in enumerate(words):
            if x in j: a.append(i)
        return a