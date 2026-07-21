class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        fin = [0]*len(temperatures)
        hottest = temperatures[-1]
        for i in range(len(temperatures) - 2, -1, -1):
            if temperatures[i] >= hottest:
                hottest = temperatures[i]
            else:
                curr = i+1
                while temperatures[curr] <= temperatures[i]:
                    curr += fin[curr]
                fin[i] = curr - i
        return fin
