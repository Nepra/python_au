# LINKED-LIST

+ [Reverse Linked List](#reverse-linked-list)
+ [Middle of the Linked List](#middle-of-the-linked-list)
+ [Palindrome Linked List](#palindrome-linked-list)
+ [Merge Two Sorted Lists](#merge-two-sorted-lists)
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

