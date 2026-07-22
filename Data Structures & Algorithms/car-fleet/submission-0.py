class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p,s] for p, s in zip(position, speed)]
        pairs.sort(reverse = True)
        stack = []
        for car in pairs:
            stack.append((target - car[0]) / car[1])
            if len(stack) >= 2:
                if stack[-1] <= stack[-2]:
                    stack.pop()
        return len(stack)