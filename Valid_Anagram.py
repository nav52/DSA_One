"""
Question

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

"""
# Solution

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        hash_s = {}
        hash_t = {}
        
        for i in range(len(s)):
            hash_s[s[i]] = 1 + hash_s.get(s[i],0)
            hash_t[t[i]] = 1 + hash_t.get(t[i],0)
        
        return hash_s == hash_t