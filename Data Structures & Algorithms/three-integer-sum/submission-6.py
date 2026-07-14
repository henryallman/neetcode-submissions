class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        for outer in range(len(nums)):
            if (outer > 0):
                if (nums[outer] == nums[outer - 1]):
                    continue
            left, right = outer + 1, len(nums) - 1
            while left < right:
                sum = nums[outer] + nums[left] + nums[right]  
                if (sum < 0):
                    left+=1
                elif (sum > 0):
                    right-=1
                else:
                    out.append([nums[outer], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                    right -= 1
            
        return out

                        


