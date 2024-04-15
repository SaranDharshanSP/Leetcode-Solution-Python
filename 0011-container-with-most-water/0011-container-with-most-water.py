class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        maz = 0
        while left<right:
            maxi = (right-left) * min(height[left],height[right])
            if maxi>maz:maz = maxi
            if height[left] < height[right]:
                left+=1
            else :right-=1
        return maz
            
