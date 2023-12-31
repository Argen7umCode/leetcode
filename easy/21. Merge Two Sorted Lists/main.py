class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    dummy = cur = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next

l1 = ListNode(0, ListNode(1, ListNode(4, ListNode(6))))
l2 = ListNode(0, ListNode(1, ListNode(4)))

l3 = mergeTwoLists(l1, l2)
current = l3
print(l3.val)
print(l3.next.val)
