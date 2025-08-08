class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f"Node({self.val}, Node({self.next})"
    
def addTwoNumbers(l1, l2):
    def rec(l1, l2, c=0):
        if not l1 and not l2 and c == 0:
            return None
        
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + c
        new_val = total % 10
        new_carry = total // 10
        
        next1 = l1.next if l1 else None
        next2 = l2.next if l2 else None
        
        return ListNode(new_val, rec(next1, next2, new_carry))
    return rec(l1, l2)

l1 = ListNode(2, ListNode(4, ListNode(9)))
l2 = ListNode(5, ListNode(6, ListNode(4, ListNode(9))))
print(addTwoNumbers(l1, l2))