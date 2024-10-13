class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return sorted(Counter(words).keys(), key=lambda word: (-Counter(words)[word], word))[:k]
