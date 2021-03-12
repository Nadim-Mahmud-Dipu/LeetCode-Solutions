# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        str1 = ""
        str2 = ""
        
        curr = l1
        while(True):
            
            str1+= str(curr.val)
            
            if curr.next == None:
                break
            curr = curr.next
        
            
        curr = l2
        while(True):
            str2+= str(curr.val)
            
            if curr.next == None:
                break
            curr = curr.next
        
        x = int(str1[::-1])
        y = int(str2[::-1])
        
        list1 = list(str(x+y))
        list1 = [int(e) for e in list1]
        
        list1.reverse()
        
        cur = dummy = ListNode(0)
        for e in list1:
            cur.next = ListNode(e)
            cur = cur.next
        return dummy.next
        
        
        
        