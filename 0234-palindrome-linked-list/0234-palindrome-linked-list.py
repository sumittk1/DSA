# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        a = []

        while head:
            a.append(head.val)
            head = head.next

        return a == a[::-1]