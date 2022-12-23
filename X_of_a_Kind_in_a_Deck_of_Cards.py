"""
Question

You are given an integer array deck where deck[i] represents the number written on the ith card.
Partition the cards into one or more groups such that:

Each group has exactly x cards where x > 1, and
All the cards in one group have the same integer written on them.
Return true if such partition is possible, or false otherwise.

Example 1:

Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].

Example 2:

Input: deck = [1,1,1,2,2,2,3,3]
Output: false
Explanation: No possible partition.

Constraints:

1 <= deck.length <= 104
0 <= deck[i] < 104
"""
#Solution

class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        deck_map ={}
        for card in deck:
            deck_map[card] = 1+deck_map.get(card, 0)
        N = len(deck)
        for i in range(2, N+1):
            if N%i == 0:
                if all(v%i == 0 for v in deck_map.values()):
                    return True
        return False
        