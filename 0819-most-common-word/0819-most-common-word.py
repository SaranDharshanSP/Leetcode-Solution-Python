class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        p = re.sub(r'[^a-zA-Z]',' ',paragraph).lower()
        p = Counter(p.split())
        for x in banned:
            if x in p:
                p.pop(x)
        return max(p,key=p.get)
