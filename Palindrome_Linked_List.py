"""
Question

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:

Input: head = [1,2,2,1]
Output: true

Example 2:

Input: head = [1,2]
Output: false 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9

"""
# Solution

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        original_pointer = head
        reverse_pointer = self.reverse_linked_list(head)
        
        while original_pointer and reverse_pointer:
            if original_pointer.val != reverse_pointer.val:
                return False
            original_pointer = original_pointer.next
            reverse_pointer = reverse_pointer.next
        
        return True
    
    def reverse_linked_list(self, head):
        if not head:
            return None
        prev = None
        pointer = head
        while pointer is not None:
            copy = ListNode(pointer.val)
            copy.next = prev
            prev = copy
            pointer = pointer.next        
        return prev