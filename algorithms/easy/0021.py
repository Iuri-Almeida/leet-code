# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 and l2:
            if l1.val <= l2.val:
                l3 = ListNode(l1.val)
                l1 = l1.next
            else:
                l3 = ListNode(l2.val)
                l2 = l2.next
            n3 = l3
            while l1 and l2:
                if l1.val <= l2.val:
                    n3.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    n3.next = ListNode(l2.val)
                    l2 = l2.next
                n3 = n3.next
            n3.next = l1 if l1 else l2
            return l3
        return l1 if l1 else l2
