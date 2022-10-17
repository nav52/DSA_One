"""
Question

Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:

Input: s = "hello"
Output: "holle"

Example 2:

Input: s = "leetcode"
Output: "leotcede"

"""
# Solution

## Stack method
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ('a','e','i','o','u','A','E','I','O','U')
        stack = []
        for letter in s:
            if letter in vowels:
                stack.append(letter)
        mid_list = []
        for i in range(len(s)):
            if s[i] in vowels:
                mid_list.append(stack.pop())
                continue
            mid_list.append(s[i])
        return ''.join(mid_list)


## Two-pointer method
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ('a','e','i','o','u','A','E','I','O','U')
        s_list = list(s)
        start = 0
        end = len(s_list)-1
        while start<end:
            if s_list[start] in vowels and s_list[end] in vowels:
                s_list[start], s_list[end] = s_list[end], s_list[start]
                start += 1
                end -= 1
            else:
                if s_list[start] not in vowels:
                    start += 1
                if s_list[end] not in vowels:
                    end -= 1
        
        return ''.join(s_list)
        