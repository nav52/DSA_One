"""
Question

Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.
Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

Example 1:

Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.

Example 2:

Input: s = "ab", goal = "ab"
Output: false
Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.

Example 3:

Input: s = "aa", goal = "aa"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.

Constraints:

1 <= s.length, goal.length <= 2 * 104
s and goal consist of lowercase letters.
"""
#Solution

class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        # Inequality case
        if len(s) != len(goal):
            return False
        
        # Equal case
        if s == goal:
            seen = set()
            for letter in s:
                if letter in seen:
                    return True
                seen.add(letter)
            return False

        # Other case (lengths are same but stings are different)
        pairs = []
        for a,b in zip(s, goal):
            if a != b:
                pairs.append([a,b])
            if len(pairs) > 2:
                return False
        return len(pairs) == 2 and pairs[0] == pairs[1][::-1]