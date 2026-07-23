from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        out = defaultdict(int)
        for num in nums:
            out[num] += 1
        freq = [[] for x in range(len(nums) + 1)]
        for num, c in out.items():
            freq[c].append(num)
        
        fin = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                fin.append(num)
                if len(fin) == k:
                    return fin
            
