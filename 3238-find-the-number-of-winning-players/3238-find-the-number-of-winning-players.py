class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        p = [{} for i in range(n)]
        for player, col in pick:
            p[player][col] = p[player].get(col, 0) + 1

        wins = 0
        for i, cols in enumerate(p):
            for count in cols.values():
                if count > i:
                    wins += 1
                    break
        return wins
                    