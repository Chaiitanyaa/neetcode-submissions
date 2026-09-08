class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        max_capacity = 0
        while l < r:
            curr_capacity = min(heights[l], heights[r]) * (r-l) 
            max_capacity = max(max_capacity,curr_capacity)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
           
        return max_capacity