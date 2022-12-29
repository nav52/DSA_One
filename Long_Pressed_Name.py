"""
Question

Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, 
and the character will be typed 1 or more times.
You examine the typed characters of the keyboard. 
Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.

Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it was not in the typed output.

Constraints:

1 <= name.length, typed.length <= 1000
name and typed consist of only lowercase English letters.
"""
#Solution

class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        idx_src= 0
        
        size_src, size_type = len(name), len(typed)
        
        for idx_type, char_type in enumerate(typed):
            
            if idx_src < size_src and name[idx_src] == char_type:
                # current type char is matched with friend's name char
                idx_src += 1 
                
            elif idx_type == 0 or typed[idx_type] != typed[idx_type-1]:
                # If first character mismatch, or it is not long-pressed repeated characters
                # Reject
                return False
        
        # Accept if all character is matched with friend name
        return idx_src == size_src