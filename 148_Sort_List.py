# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        def merge(l, r):
            h = ListNode(None)
            node = h
            while l and r:
                if l.val <= r.val:
                    node.next, l = l, l.next
                else:
                    node.next, r = r, r.next
                node = node.next
            if l:
                node.next = l
            if r:
                node.next = r
            return h.next

        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None

        # recursively run sortList until find minimum unit (1 node)
        # the flowing three lines are keys to the recursion here, I was struggling to find
        # what to return at the beginning 
        l = self.sortList(head)
        r = self.sortList(mid)
        
        return merge(l, r)
        
        
            
                        
                    
        