class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            "{": "}",
            "(": ")",
            "[": "]"
        }
        stack = []
        for i in s:
            if i in map:
                stack.append(map[i])
            else :
                if len(stack)==0:
                    return False
                a=stack.pop()
                if a!=i:
                    return False
        return len(stack)==0

