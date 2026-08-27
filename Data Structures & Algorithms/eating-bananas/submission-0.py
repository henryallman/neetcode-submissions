class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        hi = max(piles)
        lo = 1
        while lo <= hi:
            mid = (hi + lo) // 2
            time = 0
            for pile in piles:
                time += (pile + mid - 1) // mid
            if time <= h:
                hi = mid - 1
            elif time > h:
                lo = mid + 1
            else:
                return time
                
        return lo
