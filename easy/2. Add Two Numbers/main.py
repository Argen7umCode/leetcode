class ListNode:
    def __init__(self, val=None, next=None) -> None:
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self) -> None:
        self.head = None
        self.size = 0
    
    def get(self, index):
        if index >= self.size:
            return -1
        
        current = self.head
        i = 0 
        while True:
            if i == index:
                return current.val
            i += 1 
            current = current.next

    def addAtHead(self, val):
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        if index > self.size:
            return None
        elif index == 0:
            self.head = ListNode(val, self.head)
        else:
            current = self.head
            i = 0 
            while True:
                if i == index-1:
                    node = ListNode(val, current.next)
                    current.next = node
                    break
                else:
                    current = current.next
                    i += 1
        self.size += 1 
    

    def deleteAtIndex(self, index):
        if index >= self.size:
            return None
        elif index == 0:
            self.head = self.head.next
        else:
            current = self.head
            prev = None
            i = 0
            while i != index:
                prev = current
                current = current.next
                i += 1
            else:
                prev.next = current.next

        self.size -= 1
    
    def get_list_values(self):
        current = self.head
        result = []
        while current is not None:
            result.append(current.val)
            current = current.next

        return result


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()
    current = dummy
    carry = 0

    while l1 or l2:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        s = carry + x + y
        carry = s // 10
        current.next = ListNode(s % 10)
        current = current.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    if carry > 0:
        current.next = ListNode(carry)

    return dummy.next
        # return max([str_l1, str_l2])  max([str_l1, str_l2])

def get_ll_from_list(l):
    ll = MyLinkedList()
    for item in l:
        ll.addAtTail(item)
    return ll

head1 = get_ll_from_list([2,4,3]).head
head2 = get_ll_from_list([5,6,4]).head

print(addTwoNumbers(head1, head2))
