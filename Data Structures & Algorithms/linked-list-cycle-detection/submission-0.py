# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # hashtable to store seen 
        # if in seen , return false if u go all the way until head.next == none return true

        seen = {}
        curr = head
        while (curr):
            if curr in seen:
                return True
            else:
                seen[curr] = False
            curr = curr.next
        return False

