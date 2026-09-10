class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket == "(":
                stack.append(bracket)
            elif bracket == "[":
                stack.append(bracket)
            elif bracket == "{":
                stack.append(bracket)
            elif len(stack) > 0 and bracket == ")" and stack[-1] == "(":
                stack.pop()
            elif len(stack) > 0 and bracket == "]" and stack[-1] == "[":
                stack.pop()
            elif len(stack) > 0 and bracket == "}" and stack[-1] == "{":
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False
        