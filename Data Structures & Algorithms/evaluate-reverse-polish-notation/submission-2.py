class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif i == "-":
                stack.append(-int(stack.pop()) + int(stack.pop()))
            elif i == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif i == "/":
                first = stack.pop()
                stack.append(int(stack.pop()) / int(first))
            else:
                stack.append(int(i))
                print(stack)
        return int(stack.pop())