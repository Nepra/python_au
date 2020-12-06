class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def charToInt(c: str):
    if ord(c) >= ord('0') and ord(c) <= ord('9'):
        return ord(c) - ord('0')
    if ord(c) >= ord('A') and ord(c) <= ord('F'):
        return ord(c) - ord('A') + 10
    raise ValueError('Wrong input')

def intToChar(x: int):
    if x <= 9:
        return chr(x + ord('0'))
    return chr(ord('A') + x - 10)


class HexNumber:
    def __init__(self, num):
        self.head = Node(charToInt(num[len(num) - 1]))
        tail = self.head
        for i in range(len(num) - 2, -1, -1):
            tail.next = Node(charToInt(num[i]))
            tail = tail.next

    def __str__(self):
        res = ''
        cur = self.head
        while cur != None:
            res = intToChar(cur.val) + res
            cur = cur.next
        return res

    def add(self, second):
        firstSum = (self.head.val + second.head.val) % 16
        remainder = (self.head.val + second.head.val) // 16
        head = Node(firstSum)
        tail = head
        cur_first = self.head.next
        cur_second = second.head.next
        while cur_first != None and cur_second != None:
            sum = (cur_first.val + cur_second.val + remainder) % 16
            remainder = (cur_first.val + cur_second.val + remainder) // 16
            tail.next = Node(sum)
            tail = tail.next
            cur_first = cur_first.next
            cur_second = cur_second.next
        remainingNode = None
        if cur_first != None:
            remainingNode = cur_first
        if cur_second != None:
            remainingNode = cur_second
        while remainingNode != None:
            sum = (remainingNode.val + remainder) % 16
            remainder = (remainingNode.val + remainder) // 16
            tail.next = Node(sum)
            tail = tail.next
            remainingNode = remainingNode.next
        if remainder == 1:
            tail.next = Node(1)
        res = HexNumber("0")
        res.head = head
        return res


