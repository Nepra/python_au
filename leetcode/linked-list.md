# LINKED-LIST

+ [Reverse Linked List](#reverse-linked-list)
+ [Middle of the Linked List](#middle-of-the-linked-list)
+ [Palindrome Linked List](#palindrome-linked-list)
+ [Merge Two Sorted Lists](#merge-two-sorted-lists)
+ [Remove Nth Node From End of List](#remove-nth-node-from-end-of-list)
+ [Linked List Cycle II](#linked-list-cycle-ii)
+ [Linked List Cycle](#linked-list-cycle)
+ [Intersection of Two Linked Lists](#intersection-of-two-linked-lists)
+ [Sort List](#sort-list)
+ [Reorder List](#reorder-list)
<!---->
## Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/

```python
self.val = val
self.next = next
lution:
reverseList(self, head: ListNode) -> ListNode:
if head == None or head.next == None:
    return head
prev = None
while head != None:
    cur = head
    head = head.next
    cur.next = prev
    prev = cur
return prev
```

## Middle of the Linked List

https://leetcode.com/problems/middle-of-the-linked-list/

```python
self.val = val
self.next = next
lution:
middleNode(self, head: ListNode) -> ListNode:
if head.next == None:
    return head
slow = head
fast = head.next
while fast != None:
    slow = slow.next
    fast = fast.next
    if fast != None:
        fast = fast.next
return slow
```

## Palindrome Linked List

https://leetcode.com/problems/palindrome-linked-list/

```python
self.val = val
self.next = next
lution:
reverseList(self, head: ListNode) -> ListNode:
if head == None or head.next == None:
    return head
prev = None
while head != None:
    cur = head
    head = head.next
    cur.next = prev
    prev = cur
return prev
isPalindrome(self, head: ListNode) -> bool:
if head == None or head.next == None:
    return True
slow = head
fast = head
while fast != None and fast.next != None:
    fast = fast.next.next
    slow = slow.next
fast = head
slow = self.reverseList(slow)
while slow != None:
    if fast.val != slow.val:
        return False
    fast = fast.next
    slow = slow.next
return True
```

## Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/

```python
self.val = val
self.next = next
lution:
mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
head = temp = ListNode()
while l1 != None and l2 != None:
    if l1.val < l2.val:
        temp.next = l1
        l1 = l1.next
    else:
        temp.next = l2
        l2 = l2.next
    temp = temp.next
temp.next = l1 or l2
return head.next
```

## Remove Nth Node From End of List

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

```python
self.val = val
self.next = next
lution:
removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
forward = head
if forward.next == None:
    return None
for i in range (n - 1):
    forward = forward.next
if forward.next == None:
    return head.next
forward = forward.next
back = head
while forward.next != None:
    forward = forward.next
    back = back.next
back.next = back.next.next
return head
```

## Linked List Cycle II

https://leetcode.com/problems/linked-list-cycle-ii/

```python
self.val = x
self.next = None
lution:
detectCycle(self, head: ListNode) -> ListNode:
if head == None:
    return None
curTail = head
curLen = 1
while True:
    curMid = head
    for i in range(curLen - 1):
        if curMid == curTail:
            return curMid
        curMid = curMid.next
    curTail = curTail.next
    curLen += 1
    if curTail == None:
        return None
```

## Linked List Cycle

https://leetcode.com/problems/linked-list-cycle/

```python
self.val = x
self.next = None
lution:
detectCycle(self, head: ListNode) -> ListNode:
if head == None:
    return None
curTail = head
curLen = 1
while True:
    curMid = head
    for i in range(curLen - 1):
        if curMid == curTail:
            return curMid
        curMid = curMid.next
    curTail = curTail.next
    curLen += 1
    if curTail == None:
        return None
hasCycle(self, head: ListNode) -> bool:
return self.detectCycle(head) != None
```

## Intersection of Two Linked Lists

https://leetcode.com/problems/intersection-of-two-linked-lists/

```python
self.val = x
self.next = None
lution:
lenList(self, head: ListNode) -> int:
n = 0
while head != None:
    n += 1
    head = head.next
return n
getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
firstlen = self.lenList(headA)
secondlen = self.lenList(headB)
if firstlen > secondlen:
    for i in range(firstlen - secondlen):
        headA = headA.next
else:
    for i in range(secondlen - firstlen):
        headB = headB.next
while headA != None:
    if headA == headB:
        return headA
    headA, headB = headA.next, headB.next
return None
```

## Sort List

https://leetcode.com/problems/sort-list/

```python
self.val = val
self.next = next
lution:
split(self, head):
fast = slow = head
while fast.next and fast.next.next:
    fast = fast.next.next
    slow = slow.next
slow.next, slow = None, slow.next
return head, slow
mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
head = temp = ListNode()
while l1 != None and l2 != None:
    if l1.val < l2.val:
        temp.next = l1
        l1 = l1.next
    else:
        temp.next = l2
        l2 = l2.next
    temp = temp.next
temp.next = l1 or l2
return head.next
sortList(self, head: ListNode) -> ListNode:
if head == None:
    return None
if head.next == None:
    return head
l1, l2 = self.split(head)
l1 = self.sortList(l1)
l2 = self.sortList(l2)
return self.mergeTwoLists(l1, l2)
```

## Reorder List

https://leetcode.com/problems/reorder-list/

```python
self.val = val
self.next = next
lution:
reverseList(self, head: ListNode) -> ListNode:
if head == None or head.next == None:
    return head
prev = None
while head != None:
    cur = head
    head = head.next
    cur.next = prev
    prev = cur
return prev
reorderList(self, head: ListNode) -> None:
if head == None or head.next == None or head.next.next == None:
    return None
slow = head
fast = head
while fast.next != None and fast.next.next != None:
    slow = slow.next
    fast = fast.next.next
l1 = head
l2 = slow.next
slow.next = None
l2 = self.reverseList(l2)
while l2 != None:
    l1Next = l1.next
    l2Next = l2.next
    l1.next = l2
    l2.next = l1Next
    l1 = l1Next
    l2 = l2Next
return None
```

