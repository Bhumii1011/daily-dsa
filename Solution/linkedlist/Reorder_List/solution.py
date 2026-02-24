from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def ReverseList(self, head):
        prev = None
        curr = head

        while curr:
            next_node= curr.next
            curr.next = prev 
            prev = curr
            curr = next_node
        
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        if not head or not head.next:
            return 
        
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next 
        slow.next = None

        first = head
        second = self.ReverseList(second_half)

        dummy = ListNode(0)
        current = dummy

        while first or second:
            
            if first:
                current.next = first
                current = current.next
                first = first.next
            
            if second:
                current.next = second
                current = current.next
                second = second.next
        return 
    
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
    list1 = build_linked_list([1, 2, 3, 4])
    sol.reorderList(list1)
    print_linked_list(list1)