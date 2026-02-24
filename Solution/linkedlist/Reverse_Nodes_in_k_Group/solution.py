from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count =0
        temp = head

        while temp and count<k:
            count+=1
            temp = temp.next
        
        if count < k:
            return head
        
        prev = None
        curr = head

        for _ in range(k):
            next_node = curr.next
            curr.next = prev 
            prev = curr
            curr = next_node
        
        head.next = self.reverseKGroup(curr, k)

        return prev   
    

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

    print_linked_list(sol.reverseKGroup(list1, k))