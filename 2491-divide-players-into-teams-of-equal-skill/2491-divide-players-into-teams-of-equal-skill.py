class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l,r = 0, len(skill)-1
        total = skill[l]+skill[r]
        s =0
        while l<r:
            if skill[l] + skill[r] != total: return -1
            s+= skill[l] * skill[r]
            l+=1
            r-=1
        return s
