class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode):
    dummy = ListNode(0)
    cur = dummy
    while head:
        node = ListNode(head.val)
        cur.next = node
        head = head.next

    return dummy


l1 = ListNode(0, ListNode(1, ListNode(4, ListNode(6))))
l2 = reverseList(l1)