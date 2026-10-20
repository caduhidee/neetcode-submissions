# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        list = []
        while head is not None:
            list.append(head)
            head = head.next
            print(list)
            if head in list:
                return True
        return False
        