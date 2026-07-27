class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        fin = [1] * size
        
        pref, suff = 1, 1
        for i in range(size):
            fin[i] = pref
            pref *= nums[i]
        for i in range(size - 1, -1, -1):
            fin[i] *= suff
            suff *= nums[i]
        return fin