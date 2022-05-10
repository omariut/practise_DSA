
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head
    a = [head.val]
    p = head.next
    while p.next:
        a.append(p.val)
        p = p.next
    a.append(p.val)
    c = ListNode(val = a[0], next = None)
    for i in range(1, len(a)):
        c = ListNode(val = a[i], next = c)
    return c
head = ListNode(val = 1, next = ListNode(val = 2, next=ListNode(val=3, next = None)))
print(reverseList(head))

