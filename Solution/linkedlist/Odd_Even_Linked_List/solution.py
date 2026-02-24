from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
     
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            odd = head
            even = head.next
            evenhead = even
            while even and even.next:
                odd.next = even.next
                odd = odd.next
                even.next = odd.next
                even = even.next

            odd.next = evenhead

            return head
        else:
            return head
        
# 🔹 Helper function to convert list → linked list
def build_linked_list(arr):
    dummy = ListNode()
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next


# 🔹 Helper function to print linked list
def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)


if __name__ == "__main__":
    sol = Solution()
    list1 = build_linked_list([1, 2, 3, 4, 5])
    print_linked_list(sol.oddEvenList(list1))