import collections


class Solution:
    # Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        remain = collections.Counter(s)
        #bcabc b c
        for i in s:
            if i not in stack:
                while stack and i < stack[-1] and remain[stack[-1]] > 0:
                    stack.pop()
                stack.append(i)
            remain[i] -= 1
        return ''.join(stack)
