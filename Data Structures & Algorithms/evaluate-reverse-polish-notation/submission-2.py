class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                elem1 = stack.pop()
                elem2 = stack.pop()
                add = elem1 + elem2
                stack.append(add)
            elif c == "*":
                elem1 = stack.pop()
                elem2 = stack.pop()
                prod = elem1 * elem2
                stack.append(prod)
            elif c == "-":
                elem1 = stack.pop()
                elem2 = stack.pop()
                sub = elem2 - elem1
                stack.append(sub)
            elif c == "/":
                elem1 = stack.pop()
                elem2 = stack.pop()
                div = elem2 / elem1
                stack.append(int(div))
            else:
                stack.append(int(c))
        
        return stack[0]