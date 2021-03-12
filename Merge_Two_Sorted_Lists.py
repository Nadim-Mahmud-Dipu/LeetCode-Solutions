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
        
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        list1 = []
        
        while(True):
            list1.append(l1.val)
            
            if l1.next == None:
                break
            l1 = l1.next
        
        while(True):
            list1.append(l2.val)
            
            if l2.next == None:
                break
            l2 = l2.next
            
        list1 = sorted(list1)
        
        
        cur = dummy = ListNode(0)
        for e in list1:
            cur.next = ListNode(e)
            cur = cur.next
            
        return dummy.next
            
            
            
            
            