class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        cur = self.head.next
        for i in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        new = ListNode(val)
        prev_first = self.head.next
        self.head.next = new
        new.prev = self.head
        new.next = prev_first
        prev_first.prev = new
        self.length += 1
        

    def addAtTail(self, val: int) -> None:
        new = ListNode(val)
        prev_last = self.tail.prev
        prev_last.next = new
        new.prev = prev_last
        new.next = self.tail
        self.tail.prev = new
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < self.length + 1:
            new = ListNode(val)
            cur = self.head.next
            for i in range(index):
                cur = cur.next
            prev = cur.prev
            next = cur
            prev.next = new
            new.prev = prev
            new.next = next
            next.prev = new
            self.length += 1

        

    def deleteAtIndex(self, index: int) -> None:
        if index < self.length:
            cur = self.head.next

            for i in range(index):
                cur = cur.next
            prev = cur.prev
            next = cur.next
            prev.next = next
            next.prev = prev
            self.length -= 1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
