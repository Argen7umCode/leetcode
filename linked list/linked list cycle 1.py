from singly_linked_list import MyLinkedList


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: ListNode) -> bool:
    fast_pointer, slow_pointer = head, head
    i = 0
    if fast_pointer is None:
        return False

    while (fast_pointer.next != slow_pointer.next) or i == 0:
        if fast_pointer.next is None:
            return False

        fast_pointer = fast_pointer.next
        if i % 2 == 1:
            slow_pointer = slow_pointer.next
        i += 1
    else:
        return True    

def create_cycled_ll(ll, pos):
    target = None
    current = ll.head
    for i in range(ll.size-1):
        if i == pos:
            target = current
        current = current.next
    current.next = target
    return ll
        

def get_ll_from_list(l):
    ll = MyLinkedList()
    for item in l:
        ll.addAtTail(item)
    return ll

l = [1,2,3,4]
ll = get_ll_from_list(l)
new_ll = get_ll_from_list(l)

new_ll = create_cycled_ll(new_ll, 1)

assert hasCycle(new_ll.head) == True
assert hasCycle(ll.head) == False

l = [1, 2]
ll = get_ll_from_list(l)
assert hasCycle(ll.head) == False

l = [1, 1, 1, 1]
ll = get_ll_from_list(l)
assert hasCycle(ll.head) == False




# i = 0 
# current = ll.head
# while i < 10:
#     print(current.val)
#     current = current.next
#     i += 1



