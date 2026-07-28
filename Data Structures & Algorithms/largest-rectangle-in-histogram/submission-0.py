class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        marea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][-1] > h:
                popi, poph = stack.pop()
                marea = max(marea, poph * (i - popi))
                start = popi
            stack.append((start, h))
        for start, h in stack:
            marea = max(marea, h * (len(heights) - start))
        return marea