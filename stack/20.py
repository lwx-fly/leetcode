class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            "{": "}",
            "(": ")",
            "[": "]"
        }
        stack = []
        for x in s:
            if x in map:
                stack.append(map[x])
            else:
                if len(stack) != 0:
                    a = stack.pop()
                    if x != a:
                        return False
                    else:
                        continue
                else:
                    return False
        return len(stack) == 0
