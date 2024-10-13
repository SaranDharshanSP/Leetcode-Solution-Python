class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        a = []
        for i,j in points:
            a.append([(i**2)+(j**2),i,j])
        heapq.heapify(a)
        res = []
        for i in range(k):
            d,x,y = heapq.heappop(a)
            res.append([x,y])
        return res