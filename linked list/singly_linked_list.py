class NodeSLL:
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
            self.head = NodeSLL(val, self.head)
        else:
            current = self.head
            i = 0 
            while True:
                if i == index-1:
                    node = NodeSLL(val, current.next)
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


# mll.addAtHead(4)
# print(mll.get(1))
# mll.addAtHead(1)
# mll.addAtHead(5)
# mll.deleteAtIndex(3)
# mll.addAtHead(7)
# print(mll.get(3))
# print(mll.get(3))
# print(mll.get(3))
# mll.addAtHead(1)
# mll.deleteAtIndex(4)

# mll.addAtHead(2)
# mll.deleteAtIndex(1)
# mll.addAtHead(2)
# mll.addAtHead(7)
# mll.addAtHead(3)
# mll.addAtHead(2)
# mll.addAtHead(5)
# mll.addAtTail(5)
# mll.get(5)
# mll.deleteAtIndex(6)
# mll.deleteAtIndex(4)



# assert mll.addAtHead(1) is None
# print(mll.get_list_values())
# assert mll.addAtTail(3) is None
# print(mll.get_list_values())
# assert mll.addAtIndex(1, 2) is None
# print(mll.get_list_values())
# assert mll.get(1) == 2
# print(mll.get_list_values())
# assert mll.deleteAtIndex(1) is None
# print(mll.get_list_values())
# assert mll.get(1) == 3

# mll.addAtIndex(0, 10)
# print(mll.get_list_values())
# mll.addAtIndex(0, 20)
# print(mll.get_list_values())
# mll.addAtIndex(1, 30) 
# print(mll.get_list_values())
# print(mll.get(0))

# mll.addAtTail(1)
# print(mll.get(0))
# print(mll.get_list_values())




# print(mll.get(4))


