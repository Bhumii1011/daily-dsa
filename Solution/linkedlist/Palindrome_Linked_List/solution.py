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

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = self.ReverseList(slow)

        p1,p2 = head, second_half

        while p2:
            if p1.val != p2.val:
                return False
            
            p1 = p1.next
            p2 = p2.next
        
        return True
    
# 🔹 Helper function to convert list → linked list
def build_linked_list(arr):
    dummy = ListNode()
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

if __name__ == "__main__":
    sol = Solution()

    list1 = build_linked_list([1, 2, 4,2,1])
    print(sol.isPalindrome(list1))