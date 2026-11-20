# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currentElement = head

        prevElement = None
        nextElement = None

        while currentElement != None:
            nextElement = currentElement.next
            currentElement.next = prevElement
            prevElement = currentElement
            currentElement = nextElement

        return prevElement