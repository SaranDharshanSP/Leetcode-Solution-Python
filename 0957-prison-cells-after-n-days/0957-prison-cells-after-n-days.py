class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        memo = {}
        while n:
            if str(cells) in memo:
                n%=memo[str(cells)]-n
            memo[str(cells)] = n
            if n>0:
                temp = [0]*8
                for i in range(1,7):
                    if cells[i-1] == cells[i+1]:
                        temp[i] = 1
                    else: temp[i] =0
                cells = temp
                n-=1
        return cells