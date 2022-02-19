class ListNode:

    def __init__(self, val=0, next=None):

        self.val = val
        self.next = next

ListNode = ListNode()

def addTwoLists(l1: ListNode, l2: ListNode) -> ListNode:

    dummy, curr = ListNode, ListNode
    carry = 0

    while l1 or l2 or carry:

        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        val1 = v1 + v2 + carry
        carry = val1 // 10
        val1 = val1 % 10
        curr.next = ListNode(val1)

        curr = curr.next
        v1 = l1.next if l1 else None
        v2 = l2.next if l2 else None

    return dummy.next

print(addTwoLists(l1 = [2,4,3], l2 = [5,6,4]))
