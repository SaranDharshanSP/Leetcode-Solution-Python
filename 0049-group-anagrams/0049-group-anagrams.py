class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            cont = [0]*26
            for c in i:
                cont[ord(c) - ord('a')]+=1
            res[tuple(cont)].append(i)
        return res.values()
