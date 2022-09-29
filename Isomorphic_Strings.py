"""
Question

Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true

"""
# Solution

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        temp_hash = {}
        for i in range(len(s)):
            if s[i] in temp_hash:
                if temp_hash[s[i]] != t[i]:
                    return False
            else:
                if t[i] in temp_hash.values():
                    return False
                else:
                    temp_hash[s[i]] = t[i]
        return True
                    