from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head
        
        length = 1
        temp = head

        while temp.next:
            temp = temp.next
            length +=1
        
        k = k%length

        if k==0:
            return head

        no_of_nodes = length - k

        current = head
        for _ in range(1, no_of_nodes):
            current = current.next
        
        new_head = current.next
        current.next = None
        temp.next = head

        return new_head

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
    k = 2

    print_linked_list(sol.rotateRight(list1, k))