"""
Question

Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.
In the American keyboard:
    the first row consists of the characters "qwertyuiop",
    the second row consists of the characters "asdfghjkl", and
    the third row consists of the characters "zxcvbnm".

Example 1:

Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]

Example 2:

Input: words = ["omk"]
Output: []

Example 3:

Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"] 

Constraints:

1 <= words.length <= 20
1 <= words[i].length <= 100
words[i] consists of English letters (both lowercase and uppercase). 
"""
#Solution

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        letter_hash = {}
        for letter in "qwertyuiop":
            letter_hash[letter] = 1
        for letter in "asdfghjkl":
            letter_hash[letter] = 2
        for letter in "zxcvbnm":
            letter_hash[letter] = 3
        
        out_words = []
        for word in words:
            if len(word)==1:
                out_words.append(word)
                continue
            
            word_lower = word.lower()
            same=True
            for idx in range(len(word)-1):
                if letter_hash[word_lower[idx]] != letter_hash[word_lower[idx+1]]:
                    same=False
                    break
            if same:
                out_words.append(word)
            
        return out_words
        