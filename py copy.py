# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves may be changed.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k >= 2:
            cur=head
            count=0
            while cur and count<k:
                cur=cur.next
                count+=1
            if count==k:
                cur=self.reverseKGroup(cur,k)
                while count>0:
                    tmp=head.next
                    head.next=cur
                    cur=head
                    head=tmp
                    count-=1
                head=cur
        return head
