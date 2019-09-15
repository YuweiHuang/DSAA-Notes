class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '':
                continue
            else:
                if stack == []:
                    stack.append(c)
                else:
                    if (stack[-1] == '(' and c == ')') or (stack[-1] == '[' and c == ']') or (stack[-1] == '{' and c == '}'):
                        stack.pop()
                    else:
                        stack.append(c)
        if stack == []:
            return True
        else:
            return False