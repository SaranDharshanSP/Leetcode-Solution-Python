class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        scount = [0]*26
        pcount = [0]*26

        pl=len(p)
        sl=len(s)
        if pl>sl:
            return []
        
        for i in range(pl):
            pcount[ord(p[i]) - ord('a')] += 1
            scount[ord(s[i]) - ord('a')] += 1
        
        if pcount == scount:
            res.append(0)
        for i in range(pl, sl):
            scount[ord(s[i]) - ord('a')] += 1
            scount[ord(s[i - pl]) - ord('a')] -= 1
            if pcount == scount:
                res.append(i - pl + 1)
        
        return res
