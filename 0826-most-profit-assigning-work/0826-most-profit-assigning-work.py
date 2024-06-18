class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        s_worker = sorted(worker)

        i = profit =max_profit = 0

        for work in s_worker:
            while i < len(jobs) and work >= jobs[i][0]:
                profit =max(profit ,jobs[i][1])
                i+=1
            max_profit +=profit
        return max_profit

        
        