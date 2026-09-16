class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i, ele in enumerate(operations):
            if ele == '+':
                stack.append(stack[-1] + stack[-2])
            elif ele == 'C':
                stack.pop()
            elif ele == 'D':
                stack.append(2 * stack[-1])
            else:
                stack.append(int(ele))
        
        return sum(stack)