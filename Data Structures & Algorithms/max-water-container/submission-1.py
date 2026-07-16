class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maxarea = min(heights[left], heights[right]) * (right - left)
        while left < right:
            if (heights[left] < heights[right]):
                left += 1
            else:
                right -= 1
            maxarea = max(maxarea, min(heights[left], heights[right]) * (right - left))
        return maxarea