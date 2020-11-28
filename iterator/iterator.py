class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val

        if next != None:
            self.next = next

        if prev != None:
            self.prev = prev


class MyLinkedList:

    def __init__(self):
        self.head = None

    def len(self):
        if self.head == None:
            return 0
        cur = self.head
        res = 1
        cur = cur.next
        while cur != self.head:
            cur = cur.next
            res += 1
        return res

    def getNode(self, index: int) -> Node:
        cur = self.head
        if self.head == None:
            return None
        for i in range(index):
            if cur.next == self.head:
                return None
            cur = cur.next
        return cur

    def get(self, index: int) -> int:
        result = self.getNode(index)
        if result == None:
            return -1
        return result.val

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        if self.head == None:
            self.head = node
            node.next = node
            node.prev = node
        else:
            node.next = self.head
            node.prev = self.head.prev
            node.next.prev = node
            node.prev.next = node
            self.head = node

    def addAtTail(self, val: int) -> None:
        if self.head == None:
            self.addAtHead(val)
            return
        node = Node(val)
        node.prev = self.head.prev
        node.next = self.head
        node.prev.next = node
        node.next.prev = node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.len():
            self.addAtTail(val)
            return
        if index == 0:
            self.addAtHead(val)
            return
        indexth = self.getNode(index)
        if indexth == None:
            return
        node = Node(val)
        node.prev = indexth.prev
        node.next = indexth
        node.next.prev = node
        node.prev.next = node

    def deleteAtIndex(self, index: int) -> None:
        indexth = self.getNode(index)
        print(1)
        if indexth == None:
            return
        indexth.prev.next = indexth.next
        indexth.next.prev = indexth.prev
        if index == 0:
            self.head = indexth.next

    def print(self):
        if self.head == None:
            return
        cur = self.head
        res = [cur.val]
        cur = cur.next
        while cur != self.head:
            res.append(cur.val)
            cur = cur.next
        print(res)