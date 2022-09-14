"""
Question

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".


Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

"""
# Solution
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        str1 = strs[0]
        for i in range(1,len(strs)):
            ctr=0
            # Check to make sure the ctr is in bounds of both str1 and strs
            while ctr<len(str1) and ctr<len(strs[i]) and str1[ctr]==strs[i][ctr]:
                ctr+=1
            # Trim the str1 up untill the ctr as it represents the matched index
            str1=str1[:ctr]
        return str1