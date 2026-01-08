from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next



def build_linked_list(nums):
    """Convert Python list to linked list"""
    dummy = ListNode(0)
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next


def print_linked_list(node):
    """Print linked list"""
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")



if __name__ == "__main__":
    # Example: (342 + 465 = 807)
    # Stored in reverse order
    l1 = build_linked_list([2, 4, 3])
    l2 = build_linked_list([5, 6, 4])

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    print("Result Linked List:")
    print_linked_list(result)
