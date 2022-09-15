"""
Question

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    - Open brackets must be closed by the same type of brackets.
    - Open brackets must be closed in the correct order.
    - Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

"""
# Solution

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs = {')':'(', ']':'[', '}':'{'}
        for i in range(len(s)):
            if s[i] in pairs.values():
                stack.append(s[i])
            else:
                if not stack or stack[-1] != pairs[s[i]]:
                    return False
                stack.pop()
        return not stack