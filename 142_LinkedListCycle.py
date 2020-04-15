# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        # method 1: record seen node
#         if not head:
#             return None
#         record = dict()
        
#         node = head
#         while node:
#             if node not in record:
#                 record[node] = 1
#             else:
#                 return node
#             node = node.next
        
#         return None
    
        # method 2: two pointers
        if not head:
            return None
        
        sl, fa = head.next, head
        flag = False
        while sl and fa and fa.next:
            if sl == fa:
                flag = True
                break
            sl = sl.next
            fa = fa.next.next
        
        if not flag:
            return None
        
        st = head.next
        sl = sl
        while sl.next != fa:
            sl = sl.next
            st = st.next
        # now st should be at position n (n is length of cycle)
        track = head
        while track != st:
            track = track.next
            st = st.next
        return track
   
            
            
            
            
            
            