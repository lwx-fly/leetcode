class Solution:
    def isValid(self, s: str) -> bool:
        while '[]' in s or '()' in s or '{}' in s:
            s.replace('()', '').replace('{}', '').replace('[]', '')
        return not len(s)
