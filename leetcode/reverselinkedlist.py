class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    # Imperative approach, non-recursive
    node = head
    arr = []
    while True:
        arr.append(node.val)

        if node.next == None:
            break

        node = node.next

    s = node = head
    arr.reverse()
    i = 0
    while True:
        node.val = arr[i]
        i += 1

        if node.next == None:
            break

        node = node.next

    return s


head = None
for x in [1,2,3,4,5]:
    head = ListNode(x, next=head)

reverseList(head)

# Better Approach:
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        return prev
"""