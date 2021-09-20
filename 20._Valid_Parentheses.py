class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        temp = ''
        for i in s:
            if i == '(' or i == '{' or i == '[':
                brackets.append(i)
            elif len(brackets) == 0:
                return False
            else:
                temp = brackets.pop()
                if i == ')' and temp != '(':
                    return False
                if i == ']' and temp != '[':
                    return False
                if i == '}' and temp != '{':
                    return False
        if len(brackets) == 0:
            return True
        return False
